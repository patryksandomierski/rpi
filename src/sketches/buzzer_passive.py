#!/usr/bin/python
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
buzzer_id = 13
GPIO.setup(buzzer_id, GPIO.OUT)

while True:
    GPIO.output(buzzer_id, GPIO.HIGH)
    sleep(0.25)
    GPIO.output(buzzer_id, GPIO.LOW)
    sleep(1)
