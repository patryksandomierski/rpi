#!/usr/bin/python
import w1thermsensor
from w1thermsensor import W1ThermSensor
from time import sleep

allSensors = W1ThermSensor.get_available_sensors()
print(allSensors)
sensor = w1thermsensor.W1ThermSensor()

while True:
    print(sensor.get_temperature())
