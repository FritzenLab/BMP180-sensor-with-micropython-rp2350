from machine import I2C, Pin
from bmp180 import BMP180
from ssd1306 import SSD1306_I2C
import time

# I2C Setup
i2c = I2C(id=1, scl=Pin(7), sda=Pin(6), freq=100_000)

# Initialize Display (64x32 is common for 0.49")
# If your text looks scrambled, try 128x32
oled = SSD1306_I2C(64, 32, i2c)

# Initialize Sensor
bmp180 = BMP180(i2c)
bmp180.oversample_sett = 0
bmp180.baseline = 101325

initialtime = 0

while True:
    if time.ticks_diff(time.ticks_ms(), initialtime) > 2000:
        initialtime = time.ticks_ms()
        
        # Get data
        t = bmp180.temperature
        p = bmp180.pressure
        a = bmp180.altitude
        # Clear display
        oled.fill(0) 
        
        # Draw text: oled.text("string", x, y)
        oled.text("Temp:", 0, 0)
        oled.text(f"{t:.1f} C", 0, 15)
        
        # Send to screen
        oled.show()
        
        print(f"Temp: {t:.1f}")
        print(f"Pressure: {p:.1f}")
        print(f"Altitude: {a:.1f}")