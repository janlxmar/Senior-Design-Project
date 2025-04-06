import time
import pandas as pd
from tabulate import tabulate
from temp import read_temp_humidity
from soil import read_soil
from level import read_level
from light import read_light
from gas import read_gas

# Initialize DataFrame
df = pd.DataFrame(columns=[
    "Time", 
    "Temperature (C)", 
    "Humidity (%)", 
    "Moisture (%)", 
    "Liquid Level", 
    "Light (V)",
    "CO2 (ppm)",
    "TVOC (ppb)"
])

print("Starting sensor monitoring...\n")

try:
    while True:
        timestamp = time.strftime("%H:%M:%S")

        # Read all sensor data
        temp, humid = read_temp_humidity()
        moisture_data = read_soil()
        level_data = read_level()
        light_voltage = read_light()
        gas_data = read_gas()

        # --- Color-coded moisture ---
        moisture_value = moisture_data["Moisture (%)"]
        if moisture_value < 30:
            moisture_display = f"\033[91m{moisture_value:.1f}\033[0m"  # Red
        elif moisture_value < 60:
            moisture_display = f"\033[93m{moisture_value:.1f}\033[0m"  # Yellow
        else:
            moisture_display = f"\033[92m{moisture_value:.1f}\033[0m"  # Green

        # --- Color-coded liquid level ---
        level_status = level_data["Liquid Level"]
        if level_status == "Full":
            level_display = "\033[92mFull\033[0m"  # Green
        else:
            level_display = "\033[91mEmpty\033[0m"  # Red

        # --- Color-coded light ---
        if light_voltage < 1.5:
            light_display = f"\033[94m{light_voltage:.2f}\033[0m"  # Blue (Dark)
        elif light_voltage < 2.5:
            light_display = f"\033[93m{light_voltage:.2f}\033[0m"  # Yellow (Dim)
        else:
            light_display = f"\033[97m{light_voltage:.2f}\033[0m"  # White (Bright)

        # --- Safe temperature and humidity ---
        temp_display = f"{temp:.1f}" if temp is not None else "Error"
        humid_display = f"{humid:.1f}" if humid is not None else "Error"

        # --- Gas sensor ---
        co2_display = gas_data.get("CO2", "Error")
        tvoc_display = gas_data.get("TVOC", "Error")

        # Combine all readings
        new_data = {
            "Time": timestamp,
            "Temperature (C)": temp_display,
            "Humidity (%)": humid_display,
            "Moisture (%)": moisture_display,
            "Liquid Level": level_display,
            "Light (V)": light_display,
            "CO2 (ppm)": co2_display,
            "TVOC (ppb)": tvoc_display
        }

        # Append and show
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

        # Clear terminal
        print("\033c", end="")

        # Display last 10 readings
        print(tabulate(df.tail(10), headers="keys", tablefmt="github"))

        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
