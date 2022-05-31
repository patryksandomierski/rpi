#!/usr/bin/python
from collections import deque
from enum import Enum

import RPi.GPIO as GPIO
import rgb1602
import time

lcd = rgb1602.RGB1602(16, 2)
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


def main():
    lcd.setCursor(0, 0)
    lcd.printout("Pushed button:")
    btn_last_state = Button.NONE
    num = 0
    while True:
        lcd.setCursor(0, 1)
        # noinspection PyUnusedLocal
        btn_pressed = lcd_read_buttons()
        time.sleep(0.2)
        btn_pressed = lcd_read_buttons()
        if btn_last_state != Button.NONE and btn_last_state != btn_pressed:
            num += 1
            str_out = format("{}          ", str(num))
            lcd.printout(str_out)


if __name__ == '__main__':
    main()
