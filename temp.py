import board
import adafruit_dht

# initialize the DHT22 sensor on GPIO4
dht_sensor = adafruit_dht.DHT22(board.D4)

def read_temp_humidity():
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity
        return temperature, humidity
    except RuntimeError as e:
        print(f"Sensor error: {e}")
        return None, None
