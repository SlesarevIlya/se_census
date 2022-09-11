import logging
import os
import traceback
from typing import NoReturn, Tuple, List

import psycopg2

from bot.entities.user import User

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class PgUsers:
    def __init__(self, pg_creds: dict):
        self.pg_creds = pg_creds

    def _create_user_from_tuple(self, user_tuple: Tuple) -> User:
        return User(name=user_tuple[0],
                    first_name=user_tuple[1],
                    last_name=user_tuple[2],
                    bachelor_year=user_tuple[3],
                    magister_year=user_tuple[4],
                    country=user_tuple[5],
                    city=user_tuple[6],
                    company=user_tuple[7],
                    position=user_tuple[8],
                    linkedin=user_tuple[9],
                    instagram=user_tuple[10],
                    hobbies=user_tuple[11])

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

    def get_user_by_name(self, name: str) -> List[User]:
        query: str = f"select * from users where name = '{name}'"
        try:
            with psycopg2.connect(**self.pg_creds) as conn:
                with conn.cursor() as cur:
                    cur.execute(query)
                    return [self._create_user_from_tuple(user).full_meta() for user in cur.fetchall()]
        except Exception as ex:
            logger.error(str(ex))
            logger.error(traceback.format_exc())
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def get_user_by_prefix(self, name: str) -> List[User]:
        query: str = f"select * from users where name like '{name}%'"
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
