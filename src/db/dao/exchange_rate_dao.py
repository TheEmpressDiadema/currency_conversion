from src.db.dao.idao import DAO
from src.db.dao.base_dao import BaseDao

from src.db.model.exchange_rate import ExchangeRate


class ExchangeRateDao(BaseDao, DAO):
    
    def insert(self, entity: ExchangeRate):
        
        query_string = "INSERT INTO exchange_rate(base_currency_id, target_currency_id, rate, created, updated)" \
        "VALUES (?, ?, ?, ?, ?)"
        values = (entity.base_currency_id, entity.target_currency_id, entity.rate, entity.created, entity.updated)
        exception_string = "Can't insert ExchangeRate entity"
        self.execute_changes_query(query_string, values, exception_string)
        entity.id = self._get_generated_id(table_name='exchange_rate')
    
    def update(self, entity: ExchangeRate):
        
        query_string = "UPDATE exchange_rate" \
        "SET base_currency_id=?, target_currency_id=?, rate=?, updated=?" \
        "WHERE id=?"
        values = (entity.base_currency_id, entity.target_currency_id, entity.rate, entity.updated, entity.id)
        exception_string = "Can't updated ExchangeRate entity"
        self.execute_changes_query(query_string, values, exception_string)

    def delete(self, id: int):
        
        query_string = "DELETE FROM exchange_rate" \
        "WHERE id=?"
        values=(id)
        exception_string = "Can't delete ExchangeRate entity"
        self.execute_changes_query(query_string, values, exception_string)

    def get_by_id(self, id: int):
        pass

    def get_all(self):
        pass