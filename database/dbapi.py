from database.dbconnection import DbConnection


class DbAPI:
    def __init__(self, connection: DbConnection):
        self._connection = connection

    def insert(self, table: str, columns: tuple, values: tuple):
        """ """
        placeholders = ",".join("?" for _ in values)
        columns_str = ",".join(columns)
        query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"

        self._connection.executeQuery(query, values)
        self._connection.commit()

        if self._connection.isSave():
            print("Insert successful")
            return True
        else:
            print("Insert failed")
            return False

    def delete(
        self,
        table: str,
        condition_column: str = "",
        condition_value=None,
        condition: str = "=",
    ):
        """ """
        query = f"DELETE FROM {table}"
        params = ()

        if condition_column and condition_value is not None:
            query += f" WHERE {condition_column} {condition} ?"
            params = (condition_value,)

        self._connection.executeQuery(query, params)
        self._connection.commit()

        if self._connection.isSave():
            print("Delete successful")
            return True
        else:
            print("Delete failed")
            return False

    def update(
        self,
        table: str,
        columns: tuple,
        values: tuple,
        condition_column: str = "",
        condition_value=None,
        condition: str = "=",
    ):
        """ """
        columns_str = " = ?, ".join(columns)
        query = f"UPDATE {table} SET {columns_str} = ?"
        params = values

        if condition_column and condition_value is not None:
            query += f" WHERE {condition_column} {condition} ?"
            params += (condition_value,)

        self._connection.executeQuery(query, params)
        self._connection.commit()

        if self._connection.isSave():
            print("Update successful")
            return True
        else:
            print("Update failed")
            return False

    def get(
        self,
        table: str,
        columns="*",
        condition_column: str = "",
        condition_value=None,
        condition: str = "=",
    ):
        """ """
        query = f"SELECT {columns} FROM {table}"
        params = ()

        if condition_column and condition_value is not None:
            query += f" WHERE {condition_column} {condition} ?"
            params = (condition_value,)

        result = self._connection.executeQuery(query, params)
        return result

    def __exit__(self, exc_type, exc_value, traceback):
        self._connection.close()
        print("SQLite connection closed.")
