import logging

from src.db.dao.base_dao import BaseDao

from src.db.model.currency import Currency


class CurrencyDao(BaseDao):

    TABLE_NAME: str = "currency"
    INSERT_QUERY: str = "INSERT INTO currency(code, full_name, sign, created, updated) " \
            "VALUES (?, ?, ?, ?, ?)"
    UPDATE_QUERY: str = "UPDATE currency " \
        "SET code=?, full_name=?, sign=?, updated=? " \
        "WHERE id=?"
    DELETE_QUERY: str = "DELETE FROM currency " \
        "WHERE id=?"
    SELECT_SINGLE_QUERY: str = "SELECT * FROM currency WHERE id=?"
    SELECT_ALL_QUERY: str = "SELECT * FROM currency"

    def insert(self, entity: Currency):

        try:
            values = (entity.code, entity.full_name, entity.sign, entity.created, entity.updated)

            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(self.INSERT_QUERY, values)
                    connection.commit()
                    entity.id = cursor.lastrowid

        except Exception as insert_error:
            logging.error("Can't insert currency entity", insert_error)
            raise
    
    def update(self, entity: Currency):
        
        try:
            values = (entity.code, entity.full_name, entity.sign, entity.updated, entity.id)

            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(self.UPDATE_QUERY, values)
                    connection.commit()

        except Exception as update_error:
            logging.error("Can't update currency entity", update_error)
            raise

    def delete(self, id: int):

        try:
            values = (id,)

            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(self.DELETE_QUERY, values)
                    connection.commit()

        except Exception as delete_error:
            logging.error("Can't delete currency entity", delete_error)
            raise

    def get_by_id(self, id: int) -> Currency:
        
        try:
            values = (id, )

            with self._get_connection() as connection:

                with connection.cursor() as cursor:
                    cursor.execute(self.SELECT_SINGLE_QUERY, values)

                    return Currency(*cursor.fetchone())
        
        except Exception as select_single_error:
            logging.error(f"Can't select currency entity with id={id}", select_single_error)
            raise

    def get_all(self) -> list[Currency]:
        
        try:

            with self._get_connection() as connection:

                with connection.cursor() as cursor:
                    cursor.execute(self.SELECT_ALL_QUERY)
                    result = cursor.fetchall()

                    return [Currency(*row) for row in result]
        
        except Exception as select_all_error:
            logging.error("Can't select all entites from currency", select_all_error)
            raise