import time
import busio
import digitalio
import board
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn
import adafruit_mcp3xxx.mcp3008 as MCP

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP3008(spi, cs)

# channel 3 for the pH sensor
chan = AnalogIn(mcp, 3)

def read_ph():
    voltage = chan.voltage
    ph = -6.0 * voltage + 22.0 
    return round(ph, 2)

while True:
    ph_value = read_ph()
    print("pH:", ph_value)
    time.sleep(1)
