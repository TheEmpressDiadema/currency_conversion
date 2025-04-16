import sqlite3
import logging

from abc import abstractmethod

class MonoState(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class BaseDao(metaclass=MonoState):
    def __init__(self, db_path: str):
        self._db_path: str = db_path

    def _get_connection(self) -> sqlite3.Connection:
        
        try:
            return sqlite3.connect(self._db_path)
        
        except Exception as connect_error:
            logging.error(f"Can't connect {self._db_path}", connect_error)
    
    @abstractmethod
    def insert(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass