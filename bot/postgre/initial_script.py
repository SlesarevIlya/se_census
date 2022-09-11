from typing import NoReturn

from bot.credentials import postgre_creds
from bot.postgre.users import PgUsers


def main() -> NoReturn:
    pg_users = PgUsers(pg_creds=postgre_creds)
    pg_users.create_table()


if __name__ == '__main__':
    main()
