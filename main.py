#!/usr/bin/env python3
import time
from RPLCD.i2c import CharLCD
import sys

#NOTE: 0x27 may be different on your screen, refer to https://rplcd.readthedocs.io/
lcd = CharLCD('PCF8574', 0x27)
lcd.backlight_enabled = True

def main():
    time.sleep(0.05)
    # this sleep ensures no funny business with the restart
    lcd.clear()
    lcd.write_string("Input code\n\ron host...")
    foo = input("Input today\'s code: ")
    lcd.clear()
    lcd.write_string(foo)
    time.sleep(60)
    lcd.clear()
    t = 5
    while t > 0:
        lcd.clear()
        lcd.write_string("LCD_timeout" + "\n\r" + "Timeout: " + str(t))
        t -= 1
        time.sleep(1)
    
    
while True:
    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            lcd.clear()
            sys.exit(0)
