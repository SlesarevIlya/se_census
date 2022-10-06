from typing import NoReturn

from tg_bot.credentials import db_string
from tg_bot.postgres.tables.users import TableUsers


def main() -> NoReturn:
    pg_users: TableUsers = TableUsers(db=db_string)
    users_creation: bool = pg_users.create_table()
    if users_creation:
        print("users table created")
    else:
        print("smth wrong with users")


if __name__ == '__main__':
    main()
