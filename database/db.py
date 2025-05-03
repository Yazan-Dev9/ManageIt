import sqlite3


class DbConnection:
    _instance = None

    def __new__(cls, db_file: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize(db_file)
        return cls._instance

    def _initialize(self, db_file: str):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def execute_query(self, query: str, params: tuple = ()):
        """
        
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def commit(self):
        """
        
        """
        self.connection.commit()

    def close(self):
        """
        
        """
        self.connection.close()
        DbConnection._instance = None


class DbAPI:
    def __init__(self, connection: DbConnection):
        self._connection = connection

    def insert(self, table: str, columns: tuple, values: tuple):
        """
        
        """
        placeholders = ','.join('?' for _ in values)
        columns_str = ','.join(columns)
        query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
        self._connection.execute_query(query, values)
        self._connection.commit()

    def delete(self, table: str, condition_column: str = "", condition_value = None, condition: str = "="):
        """
        
        """
        query = f"DELETE FROM {table}"
        params = ()
        if condition_column and condition_value is not None:
            query += f" WHERE {condition_column} {condition} ?"
            params = (condition_value,)
        self._connection.execute_query(query, params)
        self._connection.commit()
        
    def update(self, table: str, column: str, value, condition_column: str = "", condition_value = None, condition: str = "="):
        """
        
        """
        query = f"UPDATE {table} SET {column} = ?"
        params = (value,)
        if condition_column and condition_value is not None:
            query += f" WHERE {condition_column} {condition} ?"
            params += (condition_value,)
        self._connection.execute_query(query, params)
        self._connection.commit()
        
    def get(self, table: str, columns = "*", condition_column: str = "", condition_value = None, condition: str = "="):
        """
        
        """
        query = f"SELECT {columns} FROM {table}"
        params = ()
        if condition_column and condition_value is not None:
            query += f" WHERE {condition_column} {condition} ?"
            params = (condition_value,)
        result = self._connection.execute_query(query, params)
        return result
