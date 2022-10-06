from typing import NoReturn

from bot_tg.entities.table_factory import TableFactory


def main() -> NoReturn:
    table_factory: TableFactory = TableFactory()
    users_creation: bool = table_factory.get_table("users").create_table()
    if users_creation:
        print("users table created")
    else:
        print("smth wrong with users")


if __name__ == '__main__':
    main()
