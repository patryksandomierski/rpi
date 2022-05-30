#!/usr/bin/python
import rgb1602

lcd = rgb1602.RGB1602(16, 2)  # create LCD object,specify col and row

# Print a message to the LCD.
lcd.setRGB(255, 0, 0)
lcd.setCursor(0, 0)
lcd.printout("Czesc mama")
lcd.setCursor(0, 1)
lcd.printout("Co tam w szkole")
