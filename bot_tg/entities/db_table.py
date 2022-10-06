from abc import abstractmethod
from typing import NoReturn, Any

from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Engine, Row

from bot_tg.logger import LogMixin


class DbTable(LogMixin):

    def __init__(self, db_string: str):
        self.db: Engine = create_engine(db_string)
        self.meta: MetaData = MetaData(self.db)

    @abstractmethod
    def create_table(self) -> bool:
        raise NotImplementedError("Subclasses must override method create table")

    @abstractmethod
    def insert_record(self, record) -> NoReturn:
        raise NotImplementedError("Subclasses must override method insert record")

    @abstractmethod
    def update_record(self, id, updated_dict) -> NoReturn:
        raise NotImplementedError("Subclasses must override method update record")

    @abstractmethod
    def to_entity(self, row: Row) -> Any:
        raise NotImplementedError("Subclasses must override method database row to entity")
