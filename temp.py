import board
import adafruit_dht
import time
import pandas as pd

# Initialize the DHT sensor (DHT22 on GPIO4)
dht_sensor = adafruit_dht.DHT22(board.D4)

def read_humidity():
    """Reads humidity and temperature, returns formatted data."""
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity
        timestamp = pd.Timestamp.now().strftime("%H:%M:%S")

        if temperature is not None and humidity is not None:
            return [timestamp, temperature, humidity]
    except RuntimeError:
        return None  # Ignore errors and return nothing
