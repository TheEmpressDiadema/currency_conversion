import logging

from src.db.dao.base_dao import BaseDao

from src.db.model.exchange_rate import ExchangeRate


class ExchangeRateDao(BaseDao):
    
    TABLE_NAME: str = "exchange_rate"
    INSERT_QUERY: str = "INSERT INTO exchange_rate(base_currency_id, target_currency_id, rate, created, updated) " \
        "VALUES (?, ?, ?, ?, ?)"
    UPDATE_QUERY: str = "UPDATE exchange_rate " \
        "SET base_currency_id=?, target_currency_id=?, rate=?, updated=? " \
        "WHERE id=?"
    DELETE_QUERY: str = "DELETE FROM exchange_rate" \
        "WHERE id=?"
    SELECT_SINGLE_QUERY: str = "SELECT * FROM exchange_rate WHERE id=? "
    SELECT_ALL_QUERY: str = "SELECT * FROM exchange_rate"

    def insert(self, entity: ExchangeRate):
        
        try:
            values = (entity.base_currency_id, entity.target_currency_id, entity.rate, entity.created, entity.updated)

            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(self.INSERT_QUERY, values)
                    connection.commit()
                    entity.id = cursor.lastrowid

        except Exception as insert_error:
            logging.error("Can't insert exchange rate entity", insert_error)
            raise
    
    def update(self, entity: ExchangeRate):
        
        try:
            values = (entity.base_currency_id, entity.target_currency_id, entity.rate, entity.updated, entity.id)

            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(self.UPDATE_QUERY, values)
                    connection.commit()

        except Exception as update_error:
            logging.error("Can't update exchange rate entity", update_error)
            raise

    def delete(self, id: int):
        
        try:
            values = (id, )

            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(self.DELETE_QUERY, values)
                    connection.commit()

        except Exception as delete_error:
            logging.error("Can't delete exchange rate entity", delete_error)
            raise

    def get_by_id(self, id: int) -> ExchangeRate:
        
        try:
            values = (id, )

            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(self.SELECT_SINGLE_QUERY, values)
                    return ExchangeRate(*cursor.fetchone())

        except Exception as select_single_error:
            logging.error(f"Can't select single exchange rate entity with id={id}", select_single_error)
            raise

    def get_all(self) -> list[ExchangeRate]:
        
        try:
           
            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(self.SELECT_ALL_QUERY)
                    result = cursor.fetchall()
                    return [ExchangeRate(*row) for row in result]

        except Exception as select_all_error:
            logging.error("Can't select all exchange rate entities", select_all_error)
            raise