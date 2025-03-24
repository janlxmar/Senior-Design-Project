



'''
import time
import pandas as pd
from tabulate import tabulate
from temp import read_temp_humidity
from soil import read_soil
from level import read_level

# Initialize DataFrame
df = pd.DataFrame(columns=["Time", "Temperature (°C)", "Humidity (%)", "Moisture (%)", "Liquid Level"])

print("Starting sensor monitoring...\n")

try:
    while True:
        timestamp = time.strftime("%H:%M:%S")
        temp, humid = read_temp_humidity()
        moisture = read_soil()
        level = read_level()

        # Combine all readings
        new_data = {
            "Time": timestamp,
            "Temperature (°C)": temp,
            "Humidity (%)": humid,
            "Moisture (%)": moisture["Moisture (%)"],
            "Liquid Level": level["Liquid Level"]
        }

        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

        # Clear terminal and display latest 10 readings
        print("\033c", end="")  # ANSI escape to clear screen
        print(tabulate(df.tail(10), headers="keys", tablefmt="github"))

        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
'''
