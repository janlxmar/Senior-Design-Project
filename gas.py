import time
import board
import busio
import adafruit_sgp30

def read_gas():
    # Set up I2C connection
    i2c = busio.I2C(board.SCL, board.SDA)
    sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

    # Wait a moment before initializing
    time.sleep(1.5)
    sgp30.iaq_init()
    time.sleep(1.5)  # Allow sensor to stabilize

    # Optional: set absolute humidity if you have it
    # sgp30.set_ambient_humidity(relative_humidity)

    # Wait before reading (required)
    time.sleep(1)

    # Read values
    eCO2 = sgp30.eCO2
    TVOC = sgp30.TVOC

    return {"eCO2 (ppm)": eCO2, "TVOC (ppb)": TVOC}

# Run standalone test
if __name__ == "__main__":
    try:
        while True:
            gas_data = read_gas()
            print(f"eCO2: {gas_data['eCO2 (ppm)']} ppm\tTVOC: {gas_data['TVOC (ppb)']} ppb")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped.")
