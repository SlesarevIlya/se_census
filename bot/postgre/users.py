import logging
import os
import traceback
from typing import NoReturn, Tuple

import psycopg2

from bot.entities.user import User

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class PgUsers:
    def __init__(self, pg_creds: dict):
        self.pg_creds = pg_creds

    def _create_user_from_tuple(self, user_tuple: Tuple) -> User:
        return User(id=user_tuple[0],
                    name=user_tuple[1],
                    first_name=user_tuple[2],
                    last_name=user_tuple[3],
                    bachelor_year=user_tuple[4],
                    magister_year=user_tuple[5],
                    country=user_tuple[6],
                    city=user_tuple[7],
                    company=user_tuple[8],
                    position=user_tuple[9],
                    linkedin=user_tuple[10],
                    instagram=user_tuple[11],
                    hobbies=user_tuple[12])

    def create_table(self) -> NoReturn:
        with open(os.path.join("sql", "create_users.sql")) as file:
            self.do(query=file.read(),
                    params=[],
                    log_message=f"users table created")

    def insert_user(self, user: User) -> NoReturn:
        query: str = \
            ("INSERT INTO users (id, name, first_name, last_name, bachelor_year, magister_year, country, city, company,"
             "position, linkedin, instagram, hobbies) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

        self.do(query=query,
                params=list(vars(user).values()),
                log_message=f"user {user.name} inserted")

    def update_user(self):
        pass

    def get_users_by_name(self, name: str, substring: bool):
        query: str = f"select * from users "
        if substring:
            query += f"where name like '%{name}%'"
        else:
            query += f"where name like '{name}'"
        try:
            with psycopg2.connect(**self.pg_creds) as conn:
                with conn.cursor() as cur:
                    cur.execute(query)
                    return [self._create_user_from_tuple(user) for user in cur.fetchall()]
        except Exception as ex:
            logger.error(str(ex))
            logger.error(traceback.format_exc())
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def do(self, query: str, params: list, log_message: str = "success") -> NoReturn:
        try:
            with psycopg2.connect(**self.pg_creds) as conn:
                with conn.cursor() as cur:
                    cur.execute(query, params)
                    logger.info(log_message)
        except Exception as ex:
            logger.error(str(ex))
            logger.error(traceback.format_exc())
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
