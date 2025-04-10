from src.db.dao.idao import DAO
from src.db.dao.base_dao import BaseDao

from src.db.model.currency import Currency


class CurrencyDao(BaseDao, DAO):
    
    def insert(self, entity: Currency):

        query_string = "INSERT INTO currency(code, full_name, sign, created, updated)" \
        "VALUES (?, ?, ?, ?, ?)"
        values = (entity.code, entity.full_name, entity.sign, entity.created, entity.updated)
        exception_string = "Can't insert currency entity"
        self.execute_changes_query(query_string, values, exception_string)
        entity.id = self._get_generated_id(table_name='currency')

        
    def update(self, entity: Currency):
        
        query_string = "UPDATE currency" \
        "SET code=?, full_name=?, sign=?, updated=?" \
        "WHERE id=?"
        values = (entity.code, entity.full_name, entity.sign, entity.updated, entity.id)
        exception_string = "Can't update currency entity"
        self.execute_changes_query(query_string, values, exception_string)

    def delete(self, id: int):

        query_string = "DELETE FROM currency" \
        "WHERE id=?"
        values=(id)
        exception_string = "Can't delete currency entity"
        self.execute_changes_query(query_string, values, exception_string)

    def get_by_id(self, id: int):
        
        try:

            with self.create_connection() as connection:

                query_string = "SELECT * FROM currency WHERE id=?"

                cursor = connection.cursor()
                cursor.execute(query_string, (id,))

                return Currency(*cursor.fetchone())
        
        except Exception as error_msg:

            print(f"Can't select entity with id={id}", error_msg)

    def get_all(self):
        
        try:

            with self.create_connection() as connection:

                query_string = "SELECT * FROM currency"

                cursor = connection.cursor()
                cursor.execute(query_string)
                result = cursor.fetchall()

                return [Currency(*row) for row in result]
        
        except Exception as error_msg:
            print("Can't select all from currency", error_msg)