"""

public class ShapeFactory {

   //use getShape method to get object of type shape
   public Shape getShape(String shapeType){
      if(shapeType == null){
         return null;
      }
      if(shapeType.equalsIgnoreCase("CIRCLE")){
         return new Circle();

      } else if(shapeType.equalsIgnoreCase("RECTANGLE")){
         return new Rectangle();

      } else if(shapeType.equalsIgnoreCase("SQUARE")){
         return new Square();
      }

      return null;
   }
}
"""
from typing import Union

from tg_bot.credentials import db_string
from tg_bot.entities.db_table import DbTable
from tg_bot.postgres.tables.users import TableUsers


class TableFactory:
    def get_table(self, table_type: str) -> Union[TableUsers]:
        match table_type:
            case "users":
                return TableUsers(db=db_string)
