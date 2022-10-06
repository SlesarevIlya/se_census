# se_census
## create env
```shell
python3 -m venv venv
source venv/bin/activate
pip install python-telegram-bot -U --pre
pip install -r requirements.txt
```

## server postgre
```shell
sudo -i -u postgres
service postgresql status
\l - databases
\du - users
create database census;
```

## start postgresql locally
brew services start postgresql
## terminal locally
psql postgres

## how to develop
```shell
git branch -> feature/DEV_145_communication
git update (main)
git rebase (from your branch) on main
resolve conflicts
```
## how to deploy app
```shell
ssh root@45.10.245.93
git clone https://github.com/SlesarevIlya/se_census.git
cp credentials.py se_census/bot_tg/
cd se_census/
git pull
nohup python3.10 app_tg.py &
export PYTHONPATH="/root/se_census" && python3.10 bot_tg/postgres/initial_script.py
```
