import logging
import os
import traceback
from typing import NoReturn

import psycopg2

from bot.entities.user import User

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class PgUsers:
    def __init__(self, pg_creds: dict):
        self.pg_creds = pg_creds

    def create_table(self) -> NoReturn:
        with open(os.path.join("sql", "create_users.sql")) as file:
            self.do(query=file.read(),
                    params=[],
                    log_message=f"users table created")

    def insert_user(self, user: User) -> NoReturn:
        query: str = \
            ("INSERT INTO users (name, first_name, last_name, bachelor_year, magister_year, country, city, "
             "company, position, linkedin, instagram, hobbies) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

        self.do(query=query,
                params=list(vars(user).values()),
                log_message=f"user {user.name} inserted")

    def update_user(self):
        pass

    def get_user_by_name(self, name: str):
        query: str = f"select * from users where name = '{name}'"
        try:
            with psycopg2.connect(**self.pg_creds) as conn:
                with conn.cursor() as cur:
                    cur.execute(query)
                    return cur.fetchall()
        except Exception as ex:
            logger.error(str(ex))
            logger.error(traceback.format_exc())
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def get_user_by_prefix(self, name: str):
        query: str = f"select * from users where name like '{name}%'"
        try:
            with psycopg2.connect(**self.pg_creds) as conn:
                with conn.cursor() as cur:
                    cur.execute(query)
                    return cur.fetchall()
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
