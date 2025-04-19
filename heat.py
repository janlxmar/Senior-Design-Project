from gpiozero import DigitalOutputDevice

# GPIO 5 (physical pin 29)
HEATER_PIN = 5
heater = DigitalOutputDevice(HEATER_PIN)

def turn_on_heater():
    print("Heater ON")
    heater.on()

def turn_off_heater():
    print("Heater OFF")
    heater.off()

def get_heater_status():
    return "On" if heater.value == 1 else "Off"
