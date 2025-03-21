import board
import adafruit_dht
import pandas as pd

def read_humidity():
    """Reads humidity and temperature, then releases the sensor."""
    try:
        # **Initialize sensor inside function to avoid conflicts**
        dht_sensor = adafruit_dht.DHT22(board.D4)

        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity
        timestamp = pd.Timestamp.now().strftime("%H:%M:%S")

        # **Release sensor after reading to prevent message queue errors**
        dht_sensor.exit()

        if temperature is not None and humidity is not None:
            return [timestamp, temperature, humidity]
    except RuntimeError:
        return None  # Ignore sensor read failures
