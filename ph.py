import time
import busio
import digitalio
import board
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn

# SPI setup
spi = busio.SPI(clock=board.SCLK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP3008(spi, cs)

# Use CH3 (channel 3)
chan = AnalogIn(mcp, 3)

def read_ph():
    voltage = chan.voltage
    ph = round(-6.0 * voltage + 22.0, 2)
    return voltage, ph

if __name__ == "__main__":
    try:
        while True:
            voltage, ph_val = read_ph()
            print(f"Raw: {chan.value} | Voltage: {voltage:.2f} V | pH: {ph_val}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped.")
