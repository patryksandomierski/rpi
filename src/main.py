#!/usr/bin/python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres")

cur = conn.cursor()
print('PSQL Ver:')
cur.execute('SELECT * FROM test')
print(cur.fetchall())
