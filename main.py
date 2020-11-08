#!/usr/bin/env python3
import time
from RPLCD.i2c import CharLCD
import sys

lcd = CharLCD('PCF8574', 0x27)
lcd.backlight_enabled = True

def main():
    lcd.write_string("EE0-50")
    time.sleep(999)
    
while True:
    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            lcd.clear()
            sys.exit(0)