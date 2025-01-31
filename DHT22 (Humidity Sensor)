import board
import adafruit_dht
import time

dht_sensor = adafruit_dht.DHT22(board.D4)  

while True:
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity
        print(f"Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%")
    except RuntimeError as e:
        print(f"Error: {e}")
    time.sleep(2)


//Humidity Sensor is connected to GPIO4 (Pin 7) of the Raspberry Pi
