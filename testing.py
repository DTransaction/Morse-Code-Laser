import time
import RPi.GPIO as GPIO

pins = [13]
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)
GPIO.setwarnings(False)

time_unit = 0.5

def max_voltage(): GPIO.output(pins[0], GPIO.HIGH)

def min_voltage(): GPIO.output(pins[0], GPIO.LOW)


try: 
    for x in range(10):
        max_voltage()
        time.sleep(0.5)
        min_voltage()
except Exception as E:
    print(E)
    min_voltage()
    GPIO.cleanup()

min_voltage()
GPIO.cleanup()