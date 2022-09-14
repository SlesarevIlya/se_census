# se_census
## create env
python3 -m venv venv

source venv/bin/activate

[//]: # (we need this one, because we're using pre-release api)
pip install python-telegram-bot -U --pre

pip install -r requirements.txt
## start postgresql
brew services start postgresql
## terminal
psql postgres