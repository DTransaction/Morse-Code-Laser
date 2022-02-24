import time
import RPi.GPIO as GPIO

pins = [13]
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)
GPIO.setwarnings(False)

def max_voltage(): GPIO.output(pins[0], GPIO.HIGH)

def min_voltage(): GPIO.output(pins[0], GPIO.LOW)

def laser_flash(time_units): 
    max_voltage()
    pause(time_units)
    min_voltage()
    pause(1)

def pause(multiplier):
    time.sleep(multiplier * time_unit)

def character_to_morse(character):
    sequence = morse_characters.get(character)
    for entry in sequence: 
        laser_flash(binary_to_morse_timing.get(entry))

morse_characters = {
    'a': [0, 1], 
    'b': [1, 0, 0, 0], 
    'c': [1, 0, 1, 0], 
    'd': [1, 0, 0],
    'e': [0], 
    'f': [0, 0, 1, 0], 
    'g': [1, 1, 0], 
    'h': [0, 0, 0, 0], 
    'i': [0, 0], 
    'j': [0, 1, 1, 1], 
    'k': [1, 0, 1], 
    'l': [0, 1, 0, 0], 
    'm': [1, 1], 
    'n': [1, 0], 
    'o': [1, 1, 1], 
    'p': [0, 1, 1, 0], 
    'q': [1, 1, 0, 1], 
    'r': [0, 1, 0], 
    's': [0, 0, 0], 
    't': [1], 
    'u': [0, 0, 1], 
    'v': [0, 0, 0, 1], 
    'w': [0, 1, 1], 
    'x': [1, 0, 0, 1], 
    'y': [1, 0, 1, 1], 
    'z': [1, 1, 0, 0], 
    '1': [0, 1, 1, 1, 1], 
    '2': [0, 0, 1, 1, 1], 
    '3': [0, 0, 0, 1, 1], 
    '4': [0, 0, 0, 0, 1], 
    '5': [0, 0, 0, 0, 0], 
    '6': [1, 0, 0, 0, 0], 
    '7': [1, 1, 0, 0, 0], 
    '8': [1, 1, 1, 0, 0], 
    '9': [1, 1, 1, 1, 0], 
    '0': [1, 1, 1, 1, 1]}

time_unit = 0.25

binary_to_morse_timing = {0: 1, 1: 3}

phrase = ((input("Input characters to be printed out\n> ")).lower()).split(" ")

try:
    for group in phrase: 
        for character in group:
            print(character)
            character_to_morse(character)
            pause(3)
        pause(7)
except Exception as E:
    min_voltage()
    GPIO.cleanup()
    print(E)

min_voltage()
GPIO.cleanup()