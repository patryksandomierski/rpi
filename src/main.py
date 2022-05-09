#!/usr/bin/python
import logging
from datetime import datetime, timezone
from time import sleep

import bme280
import psycopg2
import smbus2

# constants
delay_s = 1

# bme280 setup
port = 1
address = 0x76
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus, address)


def create_connection():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres")


def main():
    logging.basicConfig(level=logging.INFO)
    connection = create_connection()
    cursor = connection.cursor()
    query = """INSERT INTO climate (measure_timestamp, temperature, humidity, pressure)
        VALUES(%s, %s, %s, %s);"""
    while True:
        bme280_data = bme280.sample(bus, address)
        temperature = bme280_data.temperature
        humidity = bme280_data.humidity
        pressure = bme280_data.pressure
        logging.info("%s %s %s", temperature, humidity, pressure)
        cursor.execute(query, (datetime.now(timezone.utc), temperature, humidity, pressure))
        connection.commit()
        sleep(delay_s)


if __name__ == '__main__':
    main()
