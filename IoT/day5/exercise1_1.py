import RPi.GPIO as GPIO
from time import sleep

LED_1 = 4
LED_2 = 5
LED_3 = 14
LED_4 = 15
LEDs = [LED_1, LED_2, LED_4, LED_3]

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LEDs, GPIO.OUT, initial = False)
    print('main() program running...')

    try:
        while True:
            target = int(input("LED NUMBER: "))
            control = input("LED SET: ")
            if control == 'ON':
                GPIO.output(LEDs[target - 1], GPIO.HIGH)
            elif control == 'OFF':
                GPIO.output(LEDs[target - 1], GPIO.LOW)

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()