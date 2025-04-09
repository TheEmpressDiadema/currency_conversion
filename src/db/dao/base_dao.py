import sqlite3

class BaseDAO:

    db_folder: str = "src\db\data"
    db_url: str
    db_name: str

    def init(self, db_name: str):
        self.db_name = db_name