#!/usr/bin/python
import logging
from datetime import datetime, timezone
from time import sleep

import bme280
import psycopg2
import smbus2

# constants
delay_s = 10

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
    try:
        logging.info("starting sampling and storing data to db")
        while True:
            bme280_data = bme280.sample(bus, address)
            temperature = bme280_data.temperature
            humidity = bme280_data.humidity
            pressure = bme280_data.pressure
            logging.info("temp=%s\thumi=%s\tpress=%s", temperature, humidity, pressure)
            cursor.execute(query, (datetime.now(timezone.utc), temperature, humidity, pressure))
            connection.commit()
            sleep(delay_s)
    except KeyboardInterrupt:
        logging.info("gracefully exiting since process interrupted")
    finally:
        if connection:
            cursor.close()
            connection.close()
        logging.info("the end")


if __name__ == '__main__':
    main()
