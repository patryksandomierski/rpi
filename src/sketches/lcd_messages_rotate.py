#!/usr/bin/python
from collections import deque
from enum import Enum
from time import sleep

import bme280
import smbus2
import RPi.GPIO as GPIO
import rgb1602

# setup bme280
port = 3
address = 0x76
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus, address)
# setup lcd
lcd = rgb1602.RGB1602(16, 2)
# setup gpio buttons
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)


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


def bme280_read_data():
    data = bme280.sample(bus, address)
    temperature = data.temperature
    humidity = data.humidity
    pressure = data.pressure
    return temperature, humidity, pressure


def bme280_get_readable_data():
    temp, humi, press = bme280_read_data()
    return ['Temp.: {}'.format(f"{temp:.2f}").ljust(16),
            'Wilg.: {}'.format(f"{humi:.2f}").ljust(16),
            'Cisn.: {}'.format(f"{press:.2f}").ljust(16)]


def main():
    btn_pressed = Button.NONE

    messages = bme280_get_readable_data()
    indexes = deque(list(range(len(messages))))

    lcd_print_messages(messages, indexes)

    while True:
        messages = bme280_get_readable_data()
        btn_last_state = btn_pressed
        # noinspection PyUnusedLocal
        btn_pressed = lcd_read_buttons()
        sleep(0.2)
        btn_pressed = lcd_read_buttons()
        if btn_pressed != Button.NONE and btn_pressed != btn_last_state:
            if btn_pressed == Button.UP:
                indexes.rotate(1)
            elif btn_pressed == Button.DOWN:
                indexes.rotate(-1)
        lcd_print_messages(messages, indexes)


if __name__ == '__main__':
    main()
