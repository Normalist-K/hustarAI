import RPi.GPIO as GPIO
from time import sleep
import GPIO_EX

LED_1 = 4
LED_2 = 5
LED_3 = 14
LED_4 = 15
LEDs = [LED_1, LED_2, LED_3, LED_4]

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
                runningStep = selectRow(i+1)
                rowData[i] = readCol()
                selectRow(0)
                sleep(0.001)
                if rowData[i] != -1:
                    if i == 3:
                        if rowData[i] == 1:
                            keyData = '*'
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
    
    print(f"\r\nKeypad Data : {keyData}")
    
    return keyData

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDs, GPIO.OUT, initial = False)
    print('main() program running...')
    
    initKeypad()
    print("setup keypad pin")
    try:
        while True:
            keyData = readKeypad()
            if 1 <= keyData and keyData <= 4:
                is_ON = GPIO.input(LEDs[keyData-1])
                if is_ON:
                    GPIO.output(LEDs[keyData-1], GPIO.HIGH)
                else:
                    GPIO.output(LEDs[keyData-1], GPIO.LOW)

            
    except KeyboardInterrupt:
        GPIO.cleanup()
        
if __name__ == '__main__':
    main()
