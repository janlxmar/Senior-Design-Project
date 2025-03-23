import time
import busio
import board
import pandas as pd
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn
from digitalio import DigitalInOut, Direction

# SPI setup
spi = busio.SPI(clock=board.SCLK, MISO=board.MISO, MOSI=board.MOSI)
cs = DigitalInOut(board.D5)
mcp = MCP3008(spi, cs)

# Use channel 2 (CH2) for the non-contact level sensor
chan = AnalogIn(mcp, 2)

def read_level():
    voltage = chan.voltage
    percent = round((voltage / 3.3) * 100, 1)
    return {
        "Liquid Level (%)": percent
    }

# For testing directly
if __name__ == "__main__":
    while True:
        data = read_level()
        print(data)
        time.sleep(1)
