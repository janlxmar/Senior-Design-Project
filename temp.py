import board
import adafruit_dht
import pandas as pd
import time

def read_humidity():
    """Reads humidity and temperature, returns formatted data."""
    try:
        # **Move sensor initialization here** (prevents multiple conflicts)
        dht_sensor = adafruit_dht.DHT22(board.D4)

        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity
        timestamp = pd.Timestamp.now().strftime("%H:%M:%S")

        # **Release sensor to avoid lockups**
        dht_sensor.exit()

        if temperature is not None and humidity is not None:
            return [timestamp, temperature, humidity]
    except RuntimeError:
        return None  # Ignore errors and return nothing
