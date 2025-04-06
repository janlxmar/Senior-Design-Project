import time
import board
import busio
import adafruit_sgp30

def read_gas():
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
        sgp30.iaq_init()
        time.sleep(1)
        co2 = sgp30.eCO2
        tvoc = sgp30.TVOC
        return {
            "CO2": f"{co2} ppm",
            "TVOC": f"{tvoc} ppb"
        }
    except Exception as e:
        print(f"Gas sensor initialization failed: {e}")
        return {
            "CO2": "\033[91mError\033[0m",
            "TVOC": "\033[91mError\033[0m"
        }
        
if __name__ == "__main__":
    result = read_gas()
    print(f"CO2: {result['CO2']} | TVOC: {result['TVOC']}")
