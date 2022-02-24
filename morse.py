import time
import RPi.GPIO as GPIO

pins = [16]
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)
GPIO.setwarnings(False)

time_unit = 0.5

def max_voltage(): GPIO.output(pins[0], GPIO.HIGH)

def min_voltage(): GPIO.output(pins[0], GPIO.LOW)

def dot(): 
    max_voltage()
    time.sleep(time_unit)

def dash(): 
    min_voltage()
    time.sleep(3 * time_unit)

def pause(multiplier):
    time.sleep(multiplier * time_unit)

def character_to_morse(character):
    sequence = morse_characters.get(character)
    for entry in sequence: 
        binary_to_morse.get(entry)()

binary_to_morse = {0: dot, 1: dash}

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


test_phrase = "abc def"

test_phrase = (test_phrase.lower()).split(" ")

for group in test_phrase: 
    for character in group:
        print(character)
        character_to_morse(character)
        pause(1)
    pause(3)