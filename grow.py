import RPi.GPIO as GPIO
import time

GROW_LIGHT_PIN = 17  # we are using GPIO 17 as the output (pin 11)

GPIO.setmode(GPIO.BCM)
GPIO.setup(GROW_LIGHT_PIN, GPIO.OUT)
GPIO.output(GROW_LIGHT_PIN, GPIO.HIGH)  # assume high = not pressed

light_state = False  # False = light off, True = light on

# simulate a button press to toggle grow light power."""

def toggle_grow_light(): 
    print("Toggling grow light...")
    GPIO.output(GROW_LIGHT_PIN, GPIO.LOW)   # Simulate press
    time.sleep(0.2)
    GPIO.output(GROW_LIGHT_PIN, GPIO.HIGH)  # Release button
    time.sleep(0.2)

# turn on the grow light (only if it's off)

def turn_on_light():
    global light_state
    if not light_state:
        toggle_grow_light()
        light_state = True

# turn off the grow light (only if it's on)

def turn_off_light():
    global light_state
    if light_state:
        toggle_grow_light()
        light_state = False
        
# clean up GPIO safely when shutting down
def cleanup():
    GPIO.cleanup()
