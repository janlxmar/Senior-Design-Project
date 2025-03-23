

import board
import adafruit_dht
import time
import pandas as pd

# DHT sensor (DHT22 on GPIO4)
dht_sensor = adafruit_dht.DHT22(board.D4)  # Change to DHT11 if needed

# empty DataFrame to store sensor readings
df = pd.DataFrame(columns=["Timestamp", "Temperature (°C)", "Humidity (%)"])

print("Humidity Sensor Initialized!")

try:
    while True:
        try:
          
            temperature = dht_sensor.temperature
            humidity = dht_sensor.humidity
            timestamp = pd.Timestamp.now()

            # store the new reading in a dictionary
            new_data = {"Timestamp": timestamp, "Temperature (°C)": temperature, "Humidity (%)": humidity}

            # append to DataFrame
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

            # Display the latest DataFrame
            print(df.tail())  # Show last few readings

        except RuntimeError as e:
            print(f"Error: {e}")  # Handle occasional sensor read errors

        time.sleep(2)  # Delay between readings

except KeyboardInterrupt:
    print("\nSensor readings stopped.")
