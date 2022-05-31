#!/usr/bin/python
import threading
from collections import deque
from enum import Enum
from time import sleep

import bme280
import smbus2
import RPi.GPIO as GPIO
import rgb1602
import w1thermsensor

# setup bme280
port = 3
address = 0x76
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus, address)
# setup lcd
lcd = rgb1602.RGB1602(16, 2)
# setup gpio
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# setup gpio buttons
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# setup ds18b20
ds18b20 = w1thermsensor.W1ThermSensor()
# setup gpio buzzer
buzz_gpio_out = 13
GPIO.setup(buzz_gpio_out, GPIO.OUT)

# global sensors values
temp = 0.0
humi = 0.0
press = 0.0
probe_temp = 0.0


class Button(Enum):
    SELECT = 16
    UP = 17
    DOWN = 18
    LEFT = 19
    RIGHT = 20
    NONE = -1


def lcd_read_buttons():
    for btn in Button:
        if btn != Button.NONE:
            if GPIO.input(btn.value) == 1:
                return btn
    return Button.NONE


def lcd_print_messages(messages, indexes):
    lcd.setCursor(0, 0)
    lcd.printout(messages[indexes[0]].ljust(16))
    lcd.setCursor(0, 1)
    lcd.printout(messages[indexes[1]].ljust(16))


def bme280_read_data_thread():
    while True:
        data = bme280.sample(bus, address)
        global temp, humi, press
        temp = data.temperature
        humi = data.humidity
        press = data.pressure
        sleep(1)


def buzzer_temp_thread():
    while True:
        if probe_temp > 25.0:
            GPIO.output(buzz_gpio_out, GPIO.HIGH)
            sleep(0.25)
            GPIO.output(buzz_gpio_out, GPIO.LOW)
        else:
            GPIO.output(buzz_gpio_out, GPIO.LOW)
        sleep(5)


def get_sensors_readable_data():
    return ['Temp.     {}'.format(f"{temp:.3f}"),
            'Wilg.     {}'.format(f"{humi:.3f}"),
            'Cisn.    {}'.format(f"{press:.3f}"),
            'Temp zewn.{}'.format(f"{probe_temp:.3f}")]


def ds18b20_read_data_thread():
    while True:
        global probe_temp
        probe_temp = ds18b20.get_temperature()


def main():
    threading.Thread(target=ds18b20_read_data_thread).start()
    threading.Thread(target=bme280_read_data_thread).start()
    threading.Thread(target=buzzer_temp_thread).start()

    btn_pressed = Button.NONE
    messages = get_sensors_readable_data()
    indexes = deque(list(range(len(messages))))

    while True:
        messages = get_sensors_readable_data()
        lcd_print_messages(messages, indexes)
        btn_last_state = btn_pressed
        # noinspection PyUnusedLocal
        btn_pressed = lcd_read_buttons()
        sleep(0.1)
        btn_pressed = lcd_read_buttons()
        if btn_pressed != Button.NONE and btn_pressed != btn_last_state:
            if btn_pressed == Button.UP:
                indexes.rotate(1)
            elif btn_pressed == Button.DOWN:
                indexes.rotate(-1)


if __name__ == '__main__':
    main()
