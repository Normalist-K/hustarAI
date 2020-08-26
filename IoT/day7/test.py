import RPi.GPIO as GPIO

from flask import Flask
app = Flask(__name__)

LED_1 = 4
LED_2 = 5
LED_3 = 15
LED_4 = 14
LEDs = [LED_1, LED_2, LED_3, LED_4]

@app.route('/')
def hello():
    return "hello world"

@app.route('/led/<onoff>')
def ledonoff(onoff):
    if onoff == "on":
        print("LED Turn on")
        GPIO.output(LEDs,1)
        return "LED on"
    elif onoff == "off":
        print("LED Turn off")
        GPIO.output(LEDs,0)
        return "LED off"

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDs, GPIO.OUT, initial=GPIO.LOW)
    app.run(host='0.0.0.0', port=5000, debug=True)
