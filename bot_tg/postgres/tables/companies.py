from sqlalchemy import BigInteger, Column, Table

from bot_tg.entities.db_table import DbTable


class TableCompanies(DbTable):
    table_name: str = "companies"

    def __init__(self, db: str):
        super().__init__(db)
        self.table = Table(self.table_name, self.meta,
                           Column("id", BigInteger, primary_key=True))

    def create_table(self):
        pass

    def insert_record(self, record):
        pass

    def update_record(self, id, updated_dict):
        pass
