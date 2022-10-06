from typing import Union

from bot_tg.credentials import db_string
from bot_tg.postgres.tables.companies import TableCompanies
from bot_tg.postgres.tables.users import TableUsers


class TableFactory:
    def get_table(self, table_type: str) -> Union[TableUsers, TableCompanies]:
        match table_type:
            case "users":
                return TableUsers(db=db_string)
            case "companies":
                return TableCompanies(db=db_string)
