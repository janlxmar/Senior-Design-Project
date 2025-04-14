import RPi.GPIO as GPIO
import time

GROW_LIGHT_PIN = 17  # we are using GPIO 17 as the output (pin 11)

GPIO.setmode(GPIO.BCM)
GPIO.setup(GROW_LIGHT_PIN, GPIO.OUT)
GPIO.output(GROW_LIGHT_PIN, GPIO.HIGH)  # assume high = not pressed

def toggle_grow_light():
    print("Toggling grow light...")
    GPIO.output(GROW_LIGHT_PIN, GPIO.LOW)   # this is to simulate button press
    time.sleep(0.2)
    GPIO.output(GROW_LIGHT_PIN, GPIO.HIGH)  # release button

# Example use
toggle_grow_light()

# GPIO.cleanup()  # optional to run at the end of the script
