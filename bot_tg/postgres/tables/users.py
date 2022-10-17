import csv
from typing import Dict, List, NoReturn

from sqlalchemy import BigInteger, Column, String, Table, inspect
from sqlalchemy.engine import Row

from bot_tg.entities.db_table import DbTable
from bot_tg.entities.user import User


class TableUsers(DbTable):
    table_name: str = "users"

    def __init__(self, db: str):
        super().__init__(db)
        self.table = Table(self.table_name, self.meta,
                           Column("id", BigInteger, primary_key=True),
                           Column("name", String(256)),
                           Column("first_name", String(256)),
                           Column("last_name", String(256)),
                           Column("bachelor_year", String(256)),
                           Column("master_year", String(256)),
                           Column("country", String(256)),
                           Column("city", String(256)),
                           Column("company", String(256)),
                           Column("position", String(256)),
                           Column("linkedin", String(256)),
                           Column("instagram", String(256)),
                           Column("hobbies", String(256)))

    def get_user_by_id(self, id: str):
        pass

    def get_all(self) -> List[List[str]]:
        with self.db.connect() as conn:
            select_statement = self.table.select()

            return [self.row_to_entity(row).to_str_array() for row in conn.execute(select_statement).all()]

    def create_table(self) -> bool:
        if not inspect(self.db).has_table(self.table_name):
            with self.db.connect():
                self.table.create()
            return True

        return False

    def insert_record(self, user: User) -> NoReturn:
        with self.db.connect() as conn:
            exists_statement = self.table.select().where(self.table.columns.id == user.id)
            select_result: List[Row] = conn.execute(exists_statement).all()
            exists: bool = len(select_result) > 0

            meta_data: Dict[str, str] = dict(name=user.name,
                                             first_name=user.first_name,
                                             last_name=user.last_name,
                                             bachelor_year=user.bachelor_year,
                                             master_year=user.master_year,
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
                # TODO think about updating. Not sure that we should do that
                self.update_record(user.id, meta_data)
                self.logger.warning(f"user {user.name} updated")

    def get_record_by_name(self, name: str, substring: bool) -> List[User]:
        with self.db.connect() as conn:
            select_statement = self.table.select()
            if substring:
                select_statement = select_statement.where(name in self.table.c.name)
            else:
                select_statement = select_statement.where(self.table.c.name == name)

            return [self.row_to_entity(row) for row in conn.execute(select_statement).all()]

    def update_record(self, id: int, updated_dict: Dict[str, str]) -> NoReturn:
        with self.db.connect() as conn:
            update_statement = (self.table
                                .update()
                                .where(self.table.columns.id == id)
                                .values(updated_dict))
            conn.execute(update_statement)

    def import_from_csv(self, file_name: str) -> bool:
        with open(file_name) as file:
            reader = csv.reader(file, delimiter=',')
            [self.insert_record(self.array_to_entity(row)) for i, row in enumerate(reader) if i != 0]
            return True

    def array_to_entity(self, arr: List) -> User:
        def get_or_default(i: int) -> str:
            return arr[i] if i < len(arr) else "0"
        return User(id=int(arr[0]),
                    name=get_or_default(1),
                    first_name=get_or_default(2),
                    last_name=get_or_default(3),
                    bachelor_year=get_or_default(4),
                    master_year=get_or_default(5),
                    country=get_or_default(6),
                    city=get_or_default(7),
                    company=get_or_default(8),
                    position=get_or_default(9),
                    linkedin=get_or_default(10),
                    instagram=get_or_default(11),
                    hobbies=get_or_default(12))

    def row_to_entity(self, row: Row) -> User:
        return User(id=row.id,
                    name=row.name,
                    first_name=row.first_name,
                    last_name=row.last_name,
                    bachelor_year=row.bachelor_year,
                    master_year=row.master_year,
                    country=row.country,
                    city=row.city,
                    company=row.company,
                    position=row.position,
                    linkedin=row.linkedin,
                    instagram=row.instagram,
                    hobbies=row.hobbies)
