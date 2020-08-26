import RPi.GPIO as GPIO
from time import sleep

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route('/fan/<time>')
def fanonoff(time):
    print(f"FAN Turn on for {time} seconds")
    if time in ("1", "2", "3"):
        GPIO.output(18,1)
        sleep(time)
        GPIO.output(18,0)
    return "FAN on"
    
if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([18, 27], GPIO.OUT, initial=GPIO.LOW)
    app.run(host='0.0.0.0', port=5000, debug=True)
