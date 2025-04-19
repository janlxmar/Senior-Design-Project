from gpiozero import DigitalOutputDevice
from time import sleep

# Setup GPIO 27 (Physical Pin 13) for solenoid
solenoid = DigitalOutputDevice(27)

def water_plants(cycles=1, on_duration=1.5, off_duration=1.5):
    """
    Activates the solenoid to water plants.

    Args:
        cycles (int): Number of on/off activations
        on_duration (float): Time solenoid stays on (seconds)
        off_duration (float): Time solenoid stays off (seconds)

    Returns:
        int: 1 if watering occurred, 0 if it failed
    """
    try:
        for _ in range(cycles):
            solenoid.on()
            sleep(on_duration)
            solenoid.off()
            sleep(off_duration)
        return 1
    except:
        return 0
