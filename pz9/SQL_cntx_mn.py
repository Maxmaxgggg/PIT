import sqlite3


class SQLiteConnectionManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def __enter__(self):
        # Устанавливаем соединение с базой данных
        self.connection = sqlite3.connect(self.db_file)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        # Закрываем соединение с базой данных
        if self.connection:
            self.connection.close()
