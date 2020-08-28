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
import spidev

# flask module
from flask import Flask

# AI module
import numpy as np
import cv2
import pickle
import threading

# ETC
from time import sleep, time

# =================================================================================================
# Thread1 - Face Detection

is_Obama = False
is_stranger = True

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
    #cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))

    while(1):
        # Capture frame-by-frame
        _, frame = cap.read()
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
                        is_Obama = False
                    elif name == 'obama':
                        is_Obama = True
                    is_stranger = False
                    # added code - end
                else:
                    is_stranger = True
                
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


# =================================================================================================
# raspberry Pi control

# DHT11
dhtDevice = adafruit_dht.DHT11(board.D17)

# PIR
PIR_PIN = 7
pirState = 0

# CDS, GAS
spi = spidev.SpiDev()
CDS_CHANNEL = 0
GAS_CHANNEL = 1

def initMcp3208():
    spi.open(0, 0) # open(bus, device), device0 - GPIO8, device1 - GPIO7
    spi.max_speed_hz = 1000000
    spi.mode = 3

def buildReadCommand(channel):
    startBit = 0x04
    singleEnded = 0x08
    configBit = [startBit | ((singleEnded | (channel & 0x07)) >> 2), (channel & 0x07) << 6, 0x00]
    return configBit

def processAdcValue(result):
    byte2 = (result[1] & 0x0F)
    return (byte2 << 8) | result[2]

def analogRead(channel):
    if (channel > 7) or (channel > 8):
        return -1
    r = spi.xfer2(buildReadCommand(channel))
    adc_out = processAdcValue(r)
    return adc_out

def controlMcp3208(channel):
    analogVal = analogRead(channel)
    return analogVal

def readSensor(channel):
    return controlMcp3208(channel)

# LED
LED_1 = 4
LED_2 = 5
LED_3 = 14
LED_4 = 15
LEDs = [LED_1, LED_2, LED_4, LED_3]

# FAN
FAN = [18, 27]

# BUZZER
BUZZER_PIN = 7

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

# KEYPAD
ROW0_PIN = 0
ROW1_PIN = 1
ROW2_PIN = 2
ROW3_PIN = 3
COL0_PIN = 4
COL1_PIN = 5
COL2_PIN = 6

COL_NUM = 3
ROW_NUM = 4

g_preData = 0

colTable = [COL0_PIN, COL1_PIN, COL2_PIN]
rowTable = [ROW0_PIN, ROW1_PIN, ROW2_PIN, ROW3_PIN]

rowData = [n for n in range(ROW_NUM)]

def initKeypad():
    for i in range(0, COL_NUM):
        GPIO_EX.setup(colTable[i], GPIO_EX.IN)
    for i in range(0, ROW_NUM):
        GPIO_EX.setup(rowTable[i], GPIO_EX.OUT)

def selectRow(rowNum):
    for i in range(0, ROW_NUM):
        if rowNum == (i + 1):
            GPIO_EX.output(rowTable[i], GPIO_EX.HIGH)
            sleep(0.001)
        else:
            GPIO_EX.output(rowTable[i], GPIO_EX.LOW)
            sleep(0.001)
    return rowNum

def readCol():
    keypadstate = -1
    for i in range(0, COL_NUM):
        inputKey = GPIO_EX.input(colTable[i])
        if inputKey:
            keypadstate = keypadstate + (i + 2)
            sleep(0.5)
    return keypadstate

def readKeypad():
    global g_preData
    keyData = -1

    runningStep = selectRow(1)
    rowData[0] = readCol()
    selectRow(0)
    sleep(0.001)
    if (rowData[0] != -1):
        keyData = rowData[0]

    for i in range(1, ROW_NUM):
        if runningStep == i:
            if keyData == -1:
                runningStep = selectRow(i + 1)
                rowData[i] = readCol()
                selectRow(0)
                sleep(0.001)
                if rowData[i] != -1:
                    if i == 3:
                        if rowData[i] == 1:
                            keyData = ''
                        elif rowData[i] == 2:
                            keyData = 0
                        elif rowData[i] == 3:
                            keyData = '#'
                    else:
                        keyData = rowData[i] + (3 * i)

    sleep(0.1)

    if keyData == -1:
        return -1

    if g_preData == keyData:
        g_preData = -1
        return -1
    g_preData = keyData

    print("frnKeypad Data : {keyData}")

    return keyData

# ====================================================================================================
# Thread2 - Smart Home Control

# flag on flask request
print_temp = False
print_humi = False
print_cds = False
print_gas = False
led_on = False
fan_on = False
buzzer_on = False
pir_on = False
auto_on = False
is_chk_password = True
is_change_password = False

# AUTO MODE 
auto_obama = [1, 26, 80] # CDS voltage1, temp, humi
auto_clinton = [2, 30, 70]
pre_auto = False

def autoChk(temp, humi, cdsVolt):
    global auto_on, pre_auto, fan_on, led_on

    if auto_on:
        fan_on = False; led_on = False
        if is_Obama:
            if temp >= auto_obama[1] and humi <= auto_obama[2]:
                fan_on = True
            if cdsVolt <= auto_obama[0]:
                led_on = True
        else:
            if temp >= auto_clinton[1] and humi <= auto_clinton[2]:
                fan_on = True
            if cdsVolt <= auto_clinton[0]:
                led_on = True
        pre_auto = True
    # if auto on -> off : turn off fan and led
    else:
        if pre_auto == True:
            fan_on = False; led_on = False
        pre_auto == False

# LCD
def printLCD(temp, humi, cdsVolt, gasVal):
    global print_temp, print_humi, print_cds, print_gas
    if print_temp:
        lcd.clear()
        displayText(f"Temp.:{temp:.1f} C", 0, 0)
        print_temp = False
    
    if print_humi:
        lcd.clear()
        displayText(f"Humidity:{humi} %", 0, 0)
        print_humi = False

    if print_cds:
        lcd.clear()
        displayText(f"cds:{cdsVolt:.1f}", 0, 0)
        print_cds = False

    if print_gas:
        lcd.clear()
        displayText(f"gas:{gasVal}", 0, 0)
        print_gas = False

# led
def turnLed():
    global led_on
    if led_on:
        GPIO.output(LEDs, 1)
    else:
        GPIO.output(LEDs, 0)

# fan
def turnFan():
    global fan_on
    if fan_on:
        GPIO.output(18,1)
        GPIO.output(27,0)
    else:
        GPIO.output(18,0)
        GPIO.output(27,0)

# buzzer
def playBuzzer(pwm):
    global buzzer_on
    if buzzer_on:
        pwm.start(100)
        pwm.ChangeDutyCycle(50)
        pwm.ChangeFrequency(261)
    else:
        pwm.stop()

# pir
check_start_time = time()
check_start = False

def checkStranger():
    global buzzer_on, pir_on, check_start

    if is_stranger:
        if (time() - check_start_time) > 3:
            buzzer_on = True
            pir_on = False
            check_start = False
            lcd.clear()
    else:
        pir_on = False
        check_start = False
        lcd.clear()

def readPir():
    global pirState, check_start_time, is_stranger, check_start
    if pir_on:
        
        if check_start == False:
            check_start_time = time()
        else:
            checkStranger()

        input_state = GPIO_EX.input(PIR_PIN)
        if input_state == True:
            if pirState == 0:
                print("\r\nMotion Detected")
                lcd.clear()
                displayText("Motion Detected", 0, 0)
                
                is_stranger = True
                check_start = True
                
            pirState = 1
        else:
            if pirState == 1:
                print("\r\nMotion Ended")
                lcd.clear()
                displayText("Motion Ended", 0, 0)
            pirState = 0

# password
password = [0, 0, 0, 0]
password_chk = []
password_count = 0

def passwordChange():
    global password, is_change_password, is_chk_password
    if is_change_password:
        keyData = readKeypad()
        if keyData in range(10):
            if len(password) == 0:
                lcd.clear()
            if len(password) < 4:
                password.append(keyData)
                displayText(str(keyData), len(password) - 1, 0)
            if len(password) == 4:
                displayText("CHANGED", 0, 0)
                is_change_password = False
                is_chk_password = True
        elif keyData in ('', '#'):
            password = []
            lcd.clear()

def passwordChk():
    global is_chk_password, password, password_chk, password_count, buzzer_on, led_on
    if is_chk_password:
        keyData = readKeypad()
        if keyData in range(10):
            if len(password_chk) == 0:
                lcd.clear()
            if len(password_chk) < 4:
                password_chk.append(keyData)
                displayText(str(keyData), len(password_chk) - 1, 0)
            if len(password_chk) == 4:
                if len(password) != 4: password = [0, 0, 0, 0]
                print("----------")
                print(password)
                print(password_chk)
                if is_stranger:
                    lcd.clear()
                    displayText('ACCESS DENIED', 0, 0)
                    password_count += 1
                    if password_count >= 3:
                        buzzer_on = True
                        password_count = 0
                    password_chk = []
                else:
                    if password[::] == password_chk[::]:
                        lcd.clear()
                        displayText('CORRECT', 0, 0)
                        password_count = 0
                        password_chk = []
                        led_on = True
                    else:
                        lcd.clear()
                        displayText('FAIL', 0, 0)
                        password_count += 1
                        if password_count >= 3:
                            buzzer_on = True
                            password_count = 0
                        password_chk = []
        elif keyData in ('', '#'):
            password_chk = []
            lcd.clear()

# thread 2
def smartHome():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    initMcp3208()
    GPIO_EX.setup(PIR_PIN, GPIO_EX.IN)
    GPIO.setup(LEDs, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(FAN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    pwm = GPIO.PWM(BUZZER_PIN, 100)
    initTextlcd()
    initKeypad()
    lcd.clear()

    data_start_time = time()
    data_interval = 3 # seconds
    pre_data = False

    print("smartHome activate")

    while True:
        try:
            time_compare = (time() - data_start_time) // data_interval
            
            if time_compare % 2 == 0:
                if pre_data == False:
                    # temp = dhtDevice.temperature
                    # humi = dhtDevice.humidity
                    temp = 28
                    humi = 50
                    cdsVal = readSensor(CDS_CHANNEL)
                    cdsVolt = cdsVal * 4.096 / 4096
                    gasVal = readSensor(GAS_CHANNEL)
                    pre_data = True
            else:
                if pre_data == True:
                    pre_data = False
            
            # on-off by flags
            autoChk(temp, humi, cdsVolt)
            turnLed()
            turnFan()
            printLCD(temp, humi, cdsVolt, gasVal)            
            playBuzzer(pwm)
            readPir()
            passwordChk()
            passwordChange()

        except KeyboardInterrupt:
            lcd.clear()
            spi.close()
            GPIO.cleanup()
        except RuntimeError as error:
            print(error.args[0])

global t2
t2 = threading.Thread(target=smartHome)
t2.daemon = True
t2.start()

# =================================================================================================
# Flask Server w/ IFTTT

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

# Tell me $ (temperature, humidity, light, chemical)
@app.route('/LCD/<sensor>')
def LCD(sensor):
    global print_temp, print_humi, print_cds, print_gas

    if sensor == "temperature":
        print_temp = True
    elif sensor == "humidity":
        print_humi = True
    elif sensor == "light":
        print_cds = True
    elif sensor == "chemical":
        print_gas = True

    return "printLCD"

# Turn on $ (led, fan, buzzer, motion, auto)
# Turn off $ (led, fan, buzzer, motion, auto)
@app.route('/LED/<onoff>')
def ledOnOff(onoff):
    global led_on
    if onoff == "on":
        led_on = True
    elif onoff == "off":
        led_on = False

    return "led"

@app.route('/fan/<onoff>')
def fanOnOff(onoff):
    global fan_on
    if onoff == "on":
        fan_on = True
    elif onoff == "off":
        fan_on = False

    return "fan"

@app.route('/sound/<onoff>')
def buzzerOnOff(onoff):
    global buzzer_on
    if onoff == "on":
        buzzer_on = True
    elif onoff == "off":
        buzzer_on = False

    return "buzzer"

@app.route('/motion/<onoff>')
def pirOnOff(onoff):
    global pir_on
    if onoff == "on":
        pir_on = True
    elif onoff == "off":
        pir_on = False

    return "pir"

@app.route('/auto/<onoff>')
def autoOnOff(onoff):
    global auto_on
    if onoff == "on":
        auto_on = True
    elif onoff == "off":
        auto_on = False
    
    return 'auto'

# change password
@app.route('/password/change')
def changePassword():
    global is_chk_password, is_change_password, password
    password = []
    is_chk_password = False
    is_change_password = True

    return "password change"

# change the $ to # (brightness, temperature, humidity) 
@app.route('/auto/change/<target>/<val>')
def changeAutoVal(target, val):
    global auto_obama, auto_clinton 
    # CDS voltage1, temp, humi

    if is_Obama:
        if target == "brightness":
            auto_obama[0] = int(val)
        elif target == "temperature":
            auto_obama[1] = int(val)
        elif target == "humidity":
            auto_obama[2] = int(val)
    else:
        if target == "brightness":
            auto_clinton[0] = int(val)
        elif target == "temperature":
            auto_clinton[1] = int(val)
        elif target == "humidity":
            auto_clinton[2] = int(val)

    return "auto value change"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
        
