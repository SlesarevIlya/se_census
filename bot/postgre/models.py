from sqlalchemy import create_engine, Integer
from sqlalchemy import Table, Column, String, MetaData
from sqlalchemy.engine import Engine


class Models:
    def __init__(self, db_string: str):
        self.db: Engine = create_engine(db_string)
        self.meta: MetaData = MetaData(self.db)

    def get_users(self) -> Table:
        return Table("users2", self.meta,
                     Column("id", Integer, primary_key=True),
                     Column("name", String(256)),
                     Column("first_name", String(256)),
                     Column("last_name", String(256)),
                     Column("bachelor_year", String(256)),
                     Column("magister_year", String(256)),
                     Column("country", String(256)),
                     Column("city", String(256)),
                     Column("company", String(256)),
                     Column("position", String(256)),
                     Column("linkedin", String(256)),
                     Column("instagram", String(256)),
                     Column("hobbies", String(256)))
