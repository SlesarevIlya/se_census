# se_census
## create env
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
## start postgresql
brew services start postgresql
## terminal
psql postgres