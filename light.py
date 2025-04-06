import busio
import digitalio
import board
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn

# Setup SPI and MCP3008
spi = busio.SPI(clock=board.SCLK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)  # Or whatever pin you're using for CS
mcp = MCP3008(spi, cs)

# Create analog channel on CH3
chan = AnalogIn(mcp, 3)

def read_light():
    return round(chan.voltage, 2)
