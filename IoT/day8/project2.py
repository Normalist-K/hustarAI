# python3 exercise4.py
# ./ngrok http 5000
# googlesamples-assistant-pushtotalk

# if display error:
# export DISPLAY=:0.0
# xhost +local:root
# xhost +localhost

# smarthome module
import RPi.GPIO as GPIO
import GPIO_EX
import adafruit_dht
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

# flask module
from flask import Flask

# AI module
import numpy as np
import cv2
import pickle
import threading

# ETC
from time import sleep

# ============================================
# Face Detaction Threading

is_Obama = 0
is_stranger = 0

def faceDetact():
    global is_Obama, is_stranger

    face_cascade = cv2.CascadeClassifier('../../OpenCV-Python-Series/src/cascades/data/haarcascade_frontalface_alt2.xml')
    # eye_cascade = cv2.CascadeClassifier('../../OpenCV-Python-Series/src/cascades/data/haarcascade_eye.xml')
    # smile_cascade = cv2.CascadeClassifier('../../OpenCV-Python-Series/src/cascades/data/haarcascade_smile.xml')


    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("../../OpenCV-Python-Series/src/recognizers/face-trainner.yml")

    labels = {"person_name": 1}
    with open("../../OpenCV-Python-Series/src/pickles/face-labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}

    cap = cv2.VideoCapture(0)

    while(1):
        # Capture frame-by-frame
        ret, frame = cap.read()
        try:
            gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
            for (x, y, w, h) in faces:
                #print(x,y,w,h)
                roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
                roi_color = frame[y:y+h, x:x+w]

                # recognize? deep learned model predict keras tensorflow pytorch scikit learn
                id_, conf = recognizer.predict(roi_gray)
                if conf>=4 and conf <= 85:
                    #print(5: #id_)
                    #print(labels[id_])
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    name = labels[id_]
                    color = (255, 255, 255)
                    stroke = 2
                    cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
                    
                    # added code
                    if name == 'clinton':
                        is_Obama = 0
                    elif name == 'obama':
                        is_Obama = 1
                    is_stranger = 0
                    # added code - end
                else:
                    is_stranger = 1
                
                img_item = "7.png"
                cv2.imwrite(img_item, roi_color)

                color = (255, 0, 0) #BGR 0-255 
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
                #subitems = smile_cascade.detectMultiScale(roi_gray)
                #for (ex,ey,ew,eh) in subitems:
                #   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            # Display the resulting frame
            cv2.imshow('frame',frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        except:
            print("video error")

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

global t
t = threading.Thread(target=faceDetact)
t.daemon = True
t.start()


# ============================================
# smart home - Pi

# DHT11
dhtDevice = adafruit_dht.DHT11(board.D17)

# LED
LED_1 = 4
LED_2 = 5
LED_3 = 14
LED_4 = 15
LEDs = [LED_1, LED_2, LED_4, LED_3]

# FAN
FAN = [18, 27]

# LCD
lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D24)
lcd_d7 = digitalio.DigitalInOut(board.D21)
lcd_d6 = digitalio.DigitalInOut(board.D26)
lcd_d5 = digitalio.DigitalInOut(board.D20)
lcd_d4 = digitalio.DigitalInOut(board.D19)

lcd_columns = 16
lcd_rows = 2

lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

def initTextlcd():
    lcd.clear()
    lcd.home()
    lcd.cursor_position(0, 0)
    sleep(1.0)

def displayText(text=' ', col=0, row=0):
    lcd.cursor_position(col, row)
    lcd.message = text




def smartHome():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LEDs, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(FAN, GPIO.OUT, initial=GPIO.LOW)
    initTextlcd()

global t2
t2 = threading.Thread(target=smartHome)
t2.daemon = True
t2.start()

# ============================================
# main - flask w/ NLP

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello world"

@app.route('/ledone/<ledonoff>/<ledNum>')
def oneLed(ledonoff, ledNum):
    if ledonoff == "on":
        status = True
    if ledonoff == "off":
        status = False
        
    for idx, LED in enumerate(LEDs):
        if ledNum == str(idx+1):
            if is_Obama == 1:
                GPIO.output(LED, status)
                print(f"led {ledNum} {ledonoff}")
    return "led one"
    

@app.route('/fan/<time>')
def fanonoff(time):

    if not time.isdigit():
        return "Failed to fan on"
    
    time = int(time)
    
    if time not in (1, 2, 3):
        return "Failed to fan on"
    
    if is_Obama == 1:
        print(f"FAN Turn on for {time} seconds")
        GPIO.output(18,1)
        GPIO.output(27,0)
        sleep(time)
        GPIO.output(18,0)
        GPIO.output(27,0)

    return "FAN on"

def main():
    
    app.run(host='0.0.0.0', port=5000, debug=False)


if __name__ == "__main__":
    main()
        
