import sqlite3


class BaseDao:

    def __init__(self, db_path: str):
        self._db_path = db_path

    def create_connection(self) -> sqlite3.Connection:

        try:

            return sqlite3.connect(self._db_path)
        
        except Exception as exception:

            print(f"Can't create connection with {self.db_path}", exception)
    
    def _get_generated_id(self, table_name: str) -> int:
        
        try:

            with self.create_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(f"SELECT MAX(id) as max_id FROM {table_name}")
                result = cursor.fetchone()
                return result[0]
        
        except Exception as error_msg:

            print(f"Can't get max(id) value from {table_name}", error_msg)

    def execute_changes_query(self, query_string: str, values: tuple[any], exception_string: str):

        try: 

            with self.create_connection() as connection:

                cursor = connection.cursor()
                cursor.execute(query_string, values)
                connection.commit()
        
        except Exception as error_msg:

            print(exception_string, error_msg)