from typing import NoReturn

from bot_tg.entities.table_factory import TableFactory
from bot_tg.postgres.tables.users import TableUsers


def main() -> NoReturn:
    table_factory: TableFactory = TableFactory()

    prepare_users(table_factory)


def prepare_users(factory: TableFactory) -> NoReturn:
    users_table: TableUsers = factory.get_table("users")

    users_creation: bool = users_table.create_table()
    print("users table created") if users_creation else print("smth wrong with users")

    users_import: bool = users_table.import_from_csv("../../imports/users.csv")
    print("users imported") if users_import else print("smth wrong with import")


if __name__ == '__main__':
    main()
