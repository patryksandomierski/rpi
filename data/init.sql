CREATE TABLE climate (climate_id SERIAL NOT NULL PRIMARY KEY,
    measure_timestamp TIMESTAMP,
    temperature REAL,
    humidity REAL,
    pressure REAL
);

INSERT INTO climate (measure_timestamp, temperature, humidity, pressure) VALUES (current_timestamp - (2 * interval '1 minute'), 23.3333, 35.00000, 1024.3123);
INSERT INTO climate (measure_timestamp, temperature, humidity, pressure) VALUES (current_timestamp - (4 * interval '1 minute'), 22.3333, 32.00000, 1023.3212);
INSERT INTO climate (measure_timestamp, temperature, humidity, pressure) VALUES (current_timestamp - (6 * interval '1 minute'), 21.3333, 31.00000, 1022.3199);
INSERT INTO climate (measure_timestamp, temperature, humidity, pressure) VALUES (current_timestamp - (8 * interval '1 minute'), 20.3333, 34.00000, 1022.3123);
INSERT INTO climate (measure_timestamp, temperature, humidity, pressure) VALUES
    (current_timestamp - (10 * interval '1 minute'), RANDOM() * 10 + 15, RANDOM() *60 + 20, RANDOM() * 10 + 1015);
INSERT INTO climate (measure_timestamp, temperature, humidity, pressure) VALUES
    (current_timestamp - (12 * interval '1 minute'), RANDOM() * 10 + 15, RANDOM() *60 + 20, RANDOM() * 10 + 1015);
INSERT INTO climate (measure_timestamp, temperature, humidity, pressure) VALUES
    (current_timestamp - (14 * interval '1 minute'), RANDOM() * 10 + 15, RANDOM() *60 + 20, RANDOM() * 10 + 1015);
INSERT INTO climate (measure_timestamp, temperature, humidity, pressure) VALUES
    (current_timestamp - (16 * interval '1 minute'), RANDOM() * 10 + 15, RANDOM() *60 + 20, RANDOM() * 10 + 1015);
INSERT INTO climate (measure_timestamp, temperature, humidity, pressure) VALUES
    (current_timestamp - (18 * interval '1 minute'), RANDOM() * 10 + 15, RANDOM() *60 + 20, RANDOM() * 10 + 1015);
INSERT INTO climate (measure_timestamp, temperature, humidity, pressure) VALUES
    (current_timestamp - (20 * interval '1 minute'), RANDOM() * 10 + 15, RANDOM() *60 + 20, RANDOM() * 10 + 1015);
INSERT INTO climate (measure_timestamp, temperature, humidity, pressure) VALUES
    (current_timestamp - (22 * interval '1 minute'), RANDOM() * 10 + 15, RANDOM() *60 + 20, RANDOM() * 10 + 1015);
INSERT INTO climate (measure_timestamp, temperature, humidity, pressure) VALUES
    (current_timestamp - (24 * interval '1 minute'), RANDOM() * 10 + 15, RANDOM() *60 + 20, RANDOM() * 10 + 1015);
