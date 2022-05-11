# rpi - psql - grafana = RPG ;)

## manjaro - install before other requirements
```bash
sudo pacman -S postgresql-libs
```

## docker on rpi
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

## psycopg2 on rpi
```bash
sudo pip install psycopg2
sudo apt install python3-psycopg2
```
