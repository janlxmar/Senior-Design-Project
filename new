import time
import pandas as pd
from tabulate import tabulate
from temp import read_temp_humidity
from soil import read_soil
from level import read_level
from light import read_light
from gas import read_gas
from water import water_plants
from grow import turn_on_light, get_light_status  # grow light controls

# create the data frame
df = pd.DataFrame(columns=[
    "Time", 
    "Temperature (C)", 
    "Humidity (%)", 
    "Moisture (%)", 
    "Liquid Level", 
    "Light (V)",
    "CO2 (ppm)",
    "TVOC (ppb)",
    "Water Status",
    "Light Status"
])

print("Starting sensor monitoring...\n")

try:
    while True:
        timestamp = time.strftime("%H:%M:%S")

        # read all sensor data
        temp, humid = read_temp_humidity()
        moisture_data = read_soil()
        level_data = read_level()
        light_voltage = read_light()
        gas_data = read_gas()

        # moisture color coded
        moisture_value = moisture_data["Moisture (%)"]
        if moisture_value < 30:
            moisture_display = f"\033[91m{moisture_value:.1f}\033[0m"
        elif moisture_value < 60:
            moisture_display = f"\033[93m{moisture_value:.1f}\033[0m"
        else:
            moisture_display = f"\033[92m{moisture_value:.1f}\033[0m"

        # liquid level color coded
        level_status = level_data["Liquid Level"]
        level_display = "\033[92mFull\033[0m" if level_status == "Full" else "\033[91mEmpty\033[0m"

        # light sensor color coded
        if light_voltage < 1.5:
            light_display = f"\033[94m{light_voltage:.2f}\033[0m"
        elif light_voltage < 2.5:
            light_display = f"\033[93m{light_voltage:.2f}\033[0m"
        else:
            light_display = f"\033[97m{light_voltage:.2f}\033[0m"

        # temp and humidity
        temp_display = f"{temp:.1f}" if temp is not None else "Error"
        humid_display = f"{humid:.1f}" if humid is not None else "Error"

        # gas data
        co2_display = gas_data.get("CO2", "Error")
        tvoc_display = gas_data.get("TVOC", "Error")

        # watering status
        try:
            result = water_plants(cycles=1)
            water_status = "Watering" if result == 1 else "Idle"
        except:
            water_status = "Idle"

        # grow light status
        try:
            turn_on_light()  # simulate light being turned on (ML logic later)
            light_status = get_light_status()
        except:
            light_status = "Error"

        # combine all readings
        new_data = {
            "Time": timestamp,
            "Temperature (C)": temp_display,
            "Humidity (%)": humid_display,
            "Moisture (%)": moisture_display,
            "Liquid Level": level_display,
            "Light (V)": light_display,
            "CO2 (ppm)": co2_display,
            "TVOC (ppb)": tvoc_display,
            "Water Status": water_status,
            "Light Status": light_status
        }

        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

        # clear the terminal and show table
        print("\033c", end="")
        print(tabulate(df.tail(10), headers="keys", tablefmt="github"))

        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
