#
#
#           СКРИПТ ДЛЯ СОЗДАНИЯ И ЗАПОЛНЕНИЯ БАЗЫ ДАННЫХ
#           ПУТЬ ДО БАЗЫ ДАННЫХ ЗАДАЕТСЯ В ФАЙЛЕ PATH.INI
#
#


import configparser
from propertyContextManager import propertyContextManager
# Читаем путь до бд из конфиг-файла
config = configparser.ConfigParser()
config.read('path.ini')
path = config.get('DEFAULT', 'path')


if __name__ == "__main__":
    # Если база данных уже существует, то перезаписываем ее
    # Если нет, то она автоматически создастся
    with open(path, 'w'):
        pass
    with propertyContextManager(path) as (conn, curs):
        # Создаем таблицу 'владельцы'
        curs.execute('''
            CREATE TABLE IF NOT EXISTS owners(
                id INTEGER PRIMARY KEY UNIQUE NOT NULL,
                name TEXT NOT NULL,
                middle_name TEXT,
                surname TEXT NOT NULL,
                phoneNumber TEXT,
                dateOfBirth DATE
            )
        ''')
        # Создаем таблицу 'имущество'
        curs.execute('''
            CREATE TABLE IF NOT EXISTS property(
                id INTEGER PRIMARY KEY UNIQUE NOT NULL,
                address TEXT NOT NULL,
                propertyType TEXT NOT NULL,
                yearBuilt YEAR,
                squareMeters REAL,
                numberOfRooms INTEGER,
                owner_id INTEGER NOT NULL,
                FOREIGN KEY (owner_id) REFERENCES owners(id) ON DELETE CASCADE
                )
            ''')
        # Создаем таблицу 'пользователи'
        curs.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY UNIQUE NOT NULL,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                isAdmin BOOL NOT NULL DEFAULT 0
            )
        ''')
        #       ЗАПОЛНЯЕМ БД
        # Заполняем таблицу 'владельцы'
        curs.executemany('''
                INSERT INTO owners (name, middle_name, surname, phoneNumber, dateOfBirth)
                VALUES (?, ?, ?, ?, ?)
            ''', [
            ('John', 'H.', 'Doe', '555-1234', '1980-05-15'),
            ('Jane', None, 'Smith', '532-5678', '1975-11-30'),
            ('Albert', 'A.', 'Einstein', '555-8765', '1879-03-14'),
            ('Rododendron', 'A.', 'Belikov', '666-6666', '1980-05-15'),
            ('Tayler', 'B.', 'Samsonov', '564-1334', '1984-07-15'),
            ('Alex', 'O.', 'Antinose', '567-2834', '1982-03-13'),
            ('Bahtovar', 'F.', 'Ataev', '777-1844', '1996-04-11'),
            ('Roy', 'G.', 'Belimiligan', '123-1294', '1973-06-28'),
            ('Michel', 'M.', 'Klopyzhnikova', '579-1222', '1989-11-15'),
            ('Lena', 'B.', 'Golovach', '569-1384', '1998-12-15'),
            ('Lemeshkin', 'V.', 'Yury', '995-1200', '1996-06-25'),
            ('Bahtovar', 'B.', 'Shestakov', '591-1333', '1983-03-28'),
            ('Bibidjohn', 'B.', 'Gavrilin', '555-4444', '1975-04-19'),
        ])

        # Заполняем таблицу 'имущество' 10
        curs.executemany('''
                INSERT INTO property (address, propertyType, yearBuilt, squareMeters, numberOfRooms, owner_id)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', [
            ('123 Main St', 'House', 1990, 120.5, 3, 1),
            ('456 Oak Ave', 'Apartment', 2010, 85.0, 2, 2),
            ('789 Pine Rd', 'Villa', 1920, 350.0, 8, 3),
            ('32 Saint-Petrula Rd', 'Villa', 1920, 200.0, 5, 4),
            ('10 Kyzyl Ave', 'Villa', 1999, 150.8, 6, 5),
            ('99 Belfauzen Ave', 'House', 1941, 130.0, 4, 6),
            ('36 Vyazova St', 'Garage', 2018, 35, 0, 7),
            ('749 Saint Rd', 'Garage', 2008, 25.0, 0, 8),
            ('72 Tripack St', 'Villa', 1999, 350.0, 5, 9),
            ('999 Dota2 St', 'Villa', 2019, 250.0, 5, 10),
            ('722 Postavte-Zachet Ave', 'University', 1949, 3000, 993, 11),
            ('32 Sorana Rd', 'Flat', 2013, 50.7, 2, 12),
            ('44 Green St', 'Flat', 1989, 68.0, 2, 13),
        ])
        # Заполняем таблицу 'пользователи'
        curs.executemany('''
                INSERT INTO users (username, password, isAdmin)
                VALUES (?, ?, ?)
            ''', [
            ('admin', 'admin', True),
            ('user', 'user', False),
        ])

