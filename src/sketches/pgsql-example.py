#!/usr/bin/python
import logging
from datetime import datetime, timezone

import psycopg2


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
    cursor.execute(query, (datetime.now(timezone.utc), 100.123, 200.123, 300.123))
    connection.commit()
    cursor.close()


if __name__ == '__main__':
    main()
