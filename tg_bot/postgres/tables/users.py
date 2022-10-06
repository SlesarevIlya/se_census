from typing import Dict, NoReturn

from sqlalchemy import BigInteger, Column, String, Table, inspect

from tg_bot.entities.db_table import DbTable
from tg_bot.entities.user import User


class TableUsers(DbTable):
    table_name: str = "users"

    def __init__(self, db: str):
        super().__init__(db)
        self.table = Table(self.table_name, self.meta,
                           Column("id", BigInteger, primary_key=True),
                           Column("name", String(256)),
                           Column("first_name", String(256)),
                           Column("last_name", String(256)),
                           Column("expiration_date", String(256)),
                           Column("user_state", String(256)),
                           Column("start_communication_date", String(256)))

    def get_user_by_id(self, id: str):
        pass

    def create_table(self) -> bool:
        if not inspect(self.db).has_table(self.table_name):
            with self.db.connect():
                self.table.create()
            return True

        return False

    def insert_record(self, user: User) -> NoReturn:
        with self.db.connect() as conn:
            exists_statement = self.table.select().where(self.table.columns.id == user.id)
            exists = conn.execute(exists_statement).rowcount() > 0

            meta_data: Dict[str, str] = dict(name=user.name,
                                             first_name=user.first_name,
                                             last_name=user.last_name,
                                             bachelor_year=user.bachelor_year,
                                             magister_year=user.magister_year,
                                             country=user.country,
                                             city=user.city,
                                             company=user.company,
                                             position=user.position,
                                             linkedin=user.linkedin,
                                             instagram=user.instagram,
                                             hobbies=user.hobbies)

            if not exists:
                insert_statement = self.table.insert().values(id=user.id, **meta_data)

                conn.execute(insert_statement)
                self.logger.info(f"user {user.name} inserted")
            else:
                self.update_record(user.id, meta_data)
                self.logger.info(f"user {user.name} updated")

    def get_record_by_name(self, name: str, substring: bool) -> NoReturn:
        with self.db.connect() as conn:
            select_statement = self.table.select()
            if substring:
                select_statement = select_statement.where(name in self.table.c.name)
            else:
                select_statement = select_statement.where(self.table.c.name == name)
            result_set = conn.execute(select_statement)
            for r in result_set:
                print(r)

    def update_record(self, id: int, updated_dict: Dict[str, str]) -> NoReturn:
        with self.db.connect() as conn:
            update_statement = (self.table
                                .update()
                                .where(self.table.columns.id == id)
                                .values(updated_dict))
            conn.execute(update_statement)
