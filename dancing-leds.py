#!/usr/bin/python
import bme280
import smbus2
import RPi.GPIO as GPIO
from time import sleep

## setup bme280
port = 1
address = 0x76
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus,address)

## setup gpio leds
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

red=21
yellow=20
blue=16
green=12

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

def reset_all():
    GPIO.output(red, False)
    GPIO.output(yellow, False)
    GPIO.output(blue, False)
    GPIO.output(green, False)

def led_dance(humidity):
    if humidity > 60:
        reset_all()
        GPIO.output(red, True)
    elif humidity <= 30:
        reset_all()
        GPIO.output(green, True)
    elif humidity <= 40:
        reset_all()
        GPIO.output(blue, True)
    else:
        reset_all()
        GPIO.output(yellow, True)

while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    print(humidity, pressure, ambient_temperature)
    led_dance(humidity)
    sleep(1)
