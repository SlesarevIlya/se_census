### python 3.10 installing
guide: https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/
```shell
sudo apt update && sudo apt upgrade -y
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install python3.10 python3.10-dev python3.10-venv build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev libpq-dev
```

### postgresql installing
installation remotely guide: https://www.cherryservers.com/blog/how-to-install-and-setup-postgresql-server-on-ubuntu-20-04
```shell
sudo apt update
sudo apt install postgresql postgresql-contrib
systemctl start postgresql.service
systemctl restart postgresql
```