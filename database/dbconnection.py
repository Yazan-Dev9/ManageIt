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

    def executeQuery(self, query: str, params: tuple = ()):
        """ """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def commit(self):
        """ """
        self.connection.commit()

    def close(self):
        """ """
        self.connection.close()
        DbConnection._instance = None
