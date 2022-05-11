# rpi - psql - grafana = RPG ;)

## prerequisites on rpi4

Used in this project:
- RPi4
- bme280
- breadboard and jumper wires

### docker on rpi4

```bash
sudo apt update
sudo apt upgrade
sudo reboot
curl -fsSL https://get.docker.com -o get-docker.sh
sudo bash get-docker.sh
sudo usermod -aG docker $(whoami)
sudo reboot
docker --version
sudo pip install docker-compose
docker-compose --version
```

### psycopg2 on rpi4

```bash
sudo pip install psycopg2
sudo apt install python3-psycopg2
```

### i2c and bme280 on rpi4

Enable i2c interface using cli:
1. `sudo raspi-config`
2. `Interfacing Options`
3. `I2C`
4. ...enabled? `Yes`
5. ...reboot now? `Yes`

Install bme280 python library: `sudo pip install RPi.bme280`
If bme280 is connected to rpi, to check proper bus adress: `i2cdetect -y 1`

## local development

### manjaro - install before other requirements

```bash
sudo pacman -S postgresql-libs
```
