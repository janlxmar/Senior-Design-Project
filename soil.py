import time
import busio
import digitalio
import board
import pandas as pd
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn


spi = busio.SPI(clock=board.SCLK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP3008(spi, cs)

# channel zeroooooo
chan = AnalogIn(mcp, 0)

def read_soil():
    moisture_percent = round((chan.value / 65535) * 100, 1)
    return {
        "Moisture (%)": moisture_percent
    }

# just to test
if __name__ == "__main__":
    print("Reading soil moisture...\n")
    df = pd.DataFrame(columns=["Time", "Moisture (%)"])

    try:
        while True:
            now = pd.Timestamp.now().strftime("%H:%M:%S")
            reading = read_soil()
            reading["Time"] = now
            df = pd.concat([df, pd.DataFrame([reading])], ignore_index=True)
            print(df.tail(10).to_markdown(index=False))
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopped soil moisture monitoring.")
