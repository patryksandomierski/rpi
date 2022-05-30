# rpi + pgsql + grafana = RPG ;)

## prerequisites

Used in this project:
- RPi4 with Raspbian 11 ("heavy" version)
- bme280
- DFRobot DFR0603
- breadboard and jumper wires (I'm not an electronics engineer... :)

### docker on rpi4

```bash
sudo apt update
sudo apt upgrade
sudo reboot
curl -fsSL https://get.docker.com -o get-docker.sh
sudo bash get-docker.sh
sudo usermod -aG docker $(whoami)
sudo reboot
# verify
docker --version
sudo pip install docker-compose
# verify
docker-compose --version
```

### psycopg2 (postgres driver) on rpi4

```bash
sudo pip install psycopg2
sudo apt install python3-psycopg2
```

### i2c on rpi4

Enable i2c interface:
1. `sudo raspi-config`
2. `Interfacing Options`
3. `I2C`
4. ...enabled? `Yes`
5. ...reboot now? `Yes`

### bme280 (versatile sensor, uses i2c) on rpi4

Install bme280 python library: `sudo pip install RPi.bme280`.

If bme280 is connected to rpi, to check proper bus address, use: `i2cdetect -y $N`.
Please, refer how to setup another bus [here](#1-multiple-i2c-devices) so you can find `$N` ;)

### DFR0603 (lcd screen, uses i2c and gpio) on rpi4

Just install `sudo pip install wiringpi`, device api library is already imported from [here](https://github.com/DFRobot/DFRobot_RGB1602_RaspberryPi).

## local development

### manjaro - install before other requirements

```bash
sudo pacman -S postgresql-libs
```

### trivia

#### running

```bash
# run in background even if ssh session is closed
nohup src/main.py &
# SIGINT (same as ctrl+c for foreground app) to gracefully close process
kill -2 $(pgrep main.py)
```

#### multiple i2c devices

Add to `/boot/config.txt` e.g. `dtoverlay=i2c-gpio,bus=3,i2c_gpio_delay_us=1,i2c_gpio_sda=23,i2c_gpio_scl=27` for bus 3.

Remember to list first higher buses, e.g. 5, 4, 3. Don't use bus 0 and 2.

Pick free GPIO interfaces, e.g. DFR0603 overlay optionally reserves GPIO 16 to 20 for handling buttons.

Source: https://www.instructables.com/Raspberry-PI-Multiple-I2c-Devices/
