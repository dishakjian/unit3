import sqlite3

class DatabaseManager:
    def __init__(self, name: str):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query: str, params: tuple = ()):
        result = self.cursor.execute(query, params).fetchall()
        return result

    def save(self, query: str):
        self.cursor.execute(query)
        self.connection.commit()

    def execute(self, insert_query: str, param: tuple):
        self.cursor.execute(insert_query, param)
        self.connection.commit()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
