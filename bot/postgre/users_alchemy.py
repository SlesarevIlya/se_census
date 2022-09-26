import logging
from typing import NoReturn

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData

from bot.credentials import db_string
from bot.entities.user import User
from bot.postgre.models import Models

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class PgUsers:
    def __init__(self, db_string: str):
        self.db = create_engine(db_string)
        self.table = Models(db_string).get_users()

    def get_user_by_id(self, id: str):
        pass

    def create_table(self):
        with self.db.connect():
            self.table.create()

    def insert_record(self, user: User) -> NoReturn:
        with self.db.connect() as conn:
            insert_statement = self.table.insert().values(id=user.id,
                                                          name=user.name,
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
            conn.execute(insert_statement)
            logger.info(f"user {user.name} inserted")

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

    def update_record(self) -> NoReturn:
        with self.db.connect() as conn:
            update_statement = (self.table
                                .update()
                                .where(self.table.c.name == "i_slesarev")
                                .values(first_name="new"))
            conn.execute(update_statement)


pg = PgUsers(db_string)
pg.create_table()
