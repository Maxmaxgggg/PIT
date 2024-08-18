#
#
#           ФАЙЛ СОДЕРЖИТ МЕНЕДЖЕР КОНТЕКСТА ДЛЯ РАБОТЫ С БД
#
#


import sqlite3


# Менеджер контекста для работы с бд
class propertyContextManager:
    def __init__(self, pth: str):
        self.pth = pth

    def __enter__(self):
        self.conn = sqlite3.connect(self.pth)
        self.conn.execute('PRAGMA foreign_keys=ON;')
        self.curs = self.conn.cursor()
        return self.conn, self.curs

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
