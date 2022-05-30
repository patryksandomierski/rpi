#!/usr/bin/python
import bme280
import smbus2
from time import sleep
import rgb1602

lcd = rgb1602.RGB1602(16, 2)  # create LCD object,specify col and row

port = 3
address = 0x76  # check by `i2cdetect -y 1`
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

lcd.setRGB(192, 0, 255)

while True:
    bme280_data = bme280.sample(bus,address)
    humidity = bme280_data.humidity
    pressure = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    print(humidity, pressure, ambient_temperature)
    lcd.setCursor(0, 0)
    temp_str = "Temp: " + ambient_temperature + " oC"
    lcd.printout(temp_str)
    lcd.setCursor(0, 1)
    humidity_str = "Wilgot.: " + humidity + " %"
    lcd.printout(humidity_str)
    sleep(1)


