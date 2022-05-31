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


def lcd_print_messages(messages, indexes):
    lcd.setCursor(0, 0)
    lcd.printout(messages[indexes[0]].ljust(16))
    lcd.setCursor(0, 1)
    lcd.printout(messages[indexes[1]].ljust(16))


def main():
    btn_pressed = Button.NONE

    messages = ["1st message", "2nd message", "hoooray, im third!", "i guess im last...?"]
    indexes = deque(list(range(len(messages))))

    while True:
        lcd_print_messages(messages, indexes)
        btn_last_state = btn_pressed
        # noinspection PyUnusedLocal
        btn_pressed = lcd_read_buttons()
        time.sleep(0.2)
        btn_pressed = lcd_read_buttons()
        if btn_pressed != Button.NONE and btn_pressed != btn_last_state:
            if btn_pressed == Button.UP:
                indexes.rotate(-1)
            elif btn_pressed == Button.DOWN:
                indexes.rotate(1)
            lcd_print_messages(messages, indexes)


if __name__ == '__main__':
    main()
