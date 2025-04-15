import logging

from src.db.dao.idao import DAO
from src.db.dao.base_dao import BaseDao

from src.db.model.currency import Currency

class CurrencyDao(BaseDao, DAO):

    table_name: str = "currency"
    insert_query: str = "INSERT INTO currency(code, full_name, sign, created, updated) " \
            "VALUES (?, ?, ?, ?, ?)"
    update_query: str = "UPDATE currency " \
        "SET code=?, full_name=?, sign=?, updated=? " \
        "WHERE id=?"
    delete_query = "DELETE FROM currency " \
        "WHERE id=?"
    select_single_query = "SELECT * FROM currency WHERE id=?"
    select_all_query = "SELECT * FROM currency"

    def insert(self, entity: Currency):

        try:
            values = (entity.code, entity.full_name, entity.sign, entity.created, entity.updated)

            with self._get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(self.insert_query, values)
                connection.commit()
                entity.id = cursor.lastrowid

        except Exception as insert_error:
            logging.error("Can't insert currency entity", insert_error)
            raise
    
    def update(self, entity: Currency):
        
        try:
            values = (entity.code, entity.full_name, entity.sign, entity.updated, entity.id)

            with self._get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(self.update_query, values)
                connection.commit()

        except Exception as update_error:
            logging.error("Can't update currency entity", update_error)
            raise

    def delete(self, id: int):

        try:
            values = (id,)

            with self._get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(self.delete_query, values)
                connection.commit()

        except Exception as delete_error:
            logging.error("Can't delete currency entity", delete_error)
            raise

    def get_by_id(self, id: int) -> Currency:
        
        try:
            values = (id, )

            with self._get_connection() as connection:

                cursor = connection.cursor()
                cursor.execute(self.select_single_query, values)

                return Currency(*cursor.fetchone())
        
        except Exception as select_single_error:
            logging.error(f"Can't select currency entity with id={id}", select_single_error)
            raise

    def get_all(self) -> list[Currency]:
        
        try:

            with self._get_connection() as connection:

                cursor = connection.cursor()
                cursor.execute(self.select_all_query)
                result = cursor.fetchall()

                return [Currency(*row) for row in result]
        
        except Exception as select_all_error:
            logging.error("Can't select all entites from currency", select_all_error)