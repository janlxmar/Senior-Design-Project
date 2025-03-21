import os
import pandas as pd
import time
from temp import read_humidity

# Create an empty DataFrame with correctly named columns
df = pd.DataFrame(columns=["Time", "Temperature (C)", "Humidity (%)"])

print("🔄 Starting sensor monitoring...")

try:
    while True:
        humidity_data = read_humidity()

        if humidity_data:
            new_row = pd.DataFrame([humidity_data], columns=df.columns)
            df = pd.concat([df, new_row], ignore_index=True)

            # **Clear screen & print formatted DataFrame**
            os.system("clear")
            print(df.tail(10).to_markdown(index=False))  # Proper table formatting

        else:
            print("No valid humidity data received.")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nSensor monitoring stopped.")
