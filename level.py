import time
import busio
import board
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn
from digitalio import DigitalInOut

# set up SPI and MCP3008
spi = busio.SPI(clock=board.SCLK, MISO=board.MISO, MOSI=board.MOSI)
cs = DigitalInOut(board.D5)
mcp = MCP3008(spi, cs)

# channel twooooooooooooo
chan = AnalogIn(mcp, 2)

def read_level():
    voltage = chan.voltage
    status = "Full" if voltage > 1.5 else "Low"
    return {"Liquid Level": status}

# just a test
if __name__ == "__main__":
    while True:
        print(read_level())
        time.sleep(1)
