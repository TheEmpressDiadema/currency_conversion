import sqlite3
import logging

class BaseDao:
    def __init__(self, db_path: str):
        self._db_path = db_path

    def _get_connection(self) -> sqlite3.Connection:
        
        try:
            return sqlite3.connect(self._db_path)
        
        except Exception as connect_error:
            logging.error(f"Can't connect {self._db_path}", connect_error)