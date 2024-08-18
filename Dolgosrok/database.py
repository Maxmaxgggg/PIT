import sqlite3
import os


class ContextManager:
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        self.conn.execute('PRAGMA foreign_keys=ON;')
        self.curs = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    if os.path.exists('db/ISP.db'):
        os.remove('db/ISP.db')
    with open('db/ISP.db', 'w'):
        pass
    with ContextManager('db/ISP.db') as db:
        db.curs.execute('''
            CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY,
                userName TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                isAdmin BIT NOT NULL DEFAULT 0
            )
        ''')
        db.curs.execute('''
            CREATE TABLE IF NOT EXISTS Providers(
                id INTEGER PRIMARY KEY,
                providerName TEXT UNIQUE NOT NULL,
                userCount INTEGER,
                address TEXT,
                phoneNumber TEXT,
                email TEXT,
                website TEXT
            )
        ''')
        db.curs.execute('''
            CREATE TABLE IF NOT EXISTS Services(
                id INTEGER PRIMARY KEY,
                serviceName INTEGER,
                cost REAL,
                internetSpeed INTEGER,
                description TEXT,
                provider_id INTEGER NOT NULL,
                FOREIGN KEY (provider_id) REFERENCES Providers(id)
            )
        ''')
        db.curs.execute('''
            CREATE TABLE IF NOT EXISTS Reviews(
                id INTEGER PRIMARY KEY,
                rating INTEGER,
                comment TEXT,
                dateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                provider_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (provider_id) REFERENCES Providers(id),
                FOREIGN KEY (user_id) REFERENCES Users(id)
            )
        ''')


        provider_data1 = {
            'providerName': 'Ростелеком',
            'userCount': 1349877,
            'address': 'Москва, ул. Гончарная, д. 30, стр 1',
            'phoneNumber': '+7-800-100-08-00',
            'email': 'rostelecom@rt.ru',
            'website': 'https://msk.rt.ru/'
        }
        provider_data2 = {
            'providerName': 'МТС Home',
            'userCount': 2315671,
            'address': 'Москва, ул. Марксистская, д. 4',
            'phoneNumber': '+7-800-250-08-90',
            'email': 'info@mts.ru',
            'website': 'https://moskva.mts.ru/personal/kontaktu'
        }
        provider_data3 = {
            'providerName': 'Билайн',
            'userCount': 123312,
            'address': 'Москва, ул. Серпуховская Б., д. 17, стр. 1',
            'phoneNumber': '+7-495-974-88-88',
            'email': 'customercare@beeline.ru',
            'website': 'https://moskva.beeline.ru/customers/products/'
        }
        provider_data4 = {
            'providerName': 'Мегафон',
            'userCount': 547634,
            'address': 'Москва, ул. Академика Анохина, д. 156',
            'phoneNumber': '+7-918-543-22-54',
            'email': 'megafon@mail.ru',
            'website': 'https://moscow.megafon.ru/'
        }
        provider_data5 = {
            'providerName': 'ИнтернетВымпел',
            'userCount': 55433,
            'address': 'Москва, ул. Добронравная, д. 228',
            'phoneNumber': '+7-999-585-13-37',
            'email': 'vympelt@yandex.com',
            'website': 'https://msc.vymptlc.ru/'
        }



        # Вставляем данные провайдера в таблицу
        db.curs.execute('''
            INSERT INTO Providers(providerName, userCount, address, phoneNumber, email, website)
            VALUES (:providerName, :userCount, :address, :phoneNumber, :email, :website)
        ''', provider_data1)
        db.curs.execute('''
                    INSERT INTO Providers(providerName, userCount, address, phoneNumber, email, website)
                    VALUES (:providerName, :userCount, :address, :phoneNumber, :email, :website)
                ''', provider_data2)
        db.curs.execute('''
                            INSERT INTO Providers(providerName, userCount, address, phoneNumber, email, website)
                            VALUES (:providerName, :userCount, :address, :phoneNumber, :email, :website)
                        ''', provider_data3)
        db.curs.execute('''
                            INSERT INTO Providers(providerName, userCount, address, phoneNumber, email, website)
                            VALUES (:providerName, :userCount, :address, :phoneNumber, :email, :website)
                        ''', provider_data4)
        db.curs.execute('''
                            INSERT INTO Providers(providerName, userCount, address, phoneNumber, email, website)
                            VALUES (:providerName, :userCount, :address, :phoneNumber, :email, :website)
                        ''', provider_data5)



        service_data1 = {
            'serviceName': 'Тариф "Домашний"',
            'cost': 1199.99,
            'internetSpeed': 100,
            'description': 'Высокоскоростной интернет для вашего дома',
            'provider_id': 1  # ID провайдера из таблицы Providers
        }
        service_data2 = {
            'serviceName': 'Тариф "МегаТариф"',
            'cost': 849.99,
            'internetSpeed': 130,
            'description': 'Один из самых быстрых интернетов на территории города',
            'provider_id': 2  # ID провайдера из таблицы Providers
        }
        service_data3 = {
            'serviceName': 'Тариф "Супер"',
            'cost': 599.99,
            'internetSpeed': 60,
            'description': 'Стабильный и надежный интернет',
            'provider_id': 3  # ID провайдера из таблицы Providers
        }
        service_data4 = {
            'serviceName': 'Тариф "Бомба"',
            'cost': 1799.99,
            'internetSpeed': 600,
            'description': 'Высокоскоростной интернет для офисов',
            'provider_id': 4  # ID провайдера из таблицы Providers
        }
        service_data5 = {
            'serviceName': 'Тариф "OnLine"',
            'cost': 799.99,
            'internetSpeed': 50,
            'description': 'Стабильный интернет в ваш дом',
            'provider_id': 5  # ID провайдера из таблицы Providers
        }

        # Вставка данных новой услуги в таблицу Services
        db.curs.execute('''
            INSERT INTO Services(serviceName, cost, internetSpeed, description, provider_id)
            VALUES (:serviceName, :cost, :internetSpeed, :description, :provider_id)
        ''', service_data1)
        db.curs.execute('''
                   INSERT INTO Services(serviceName, cost, internetSpeed, description, provider_id)
                    VALUES (:serviceName, :cost, :internetSpeed, :description, :provider_id)
                ''', service_data2)
        db.curs.execute('''
                           INSERT INTO Services(serviceName, cost, internetSpeed, description, provider_id)
                            VALUES (:serviceName, :cost, :internetSpeed, :description, :provider_id)
                        ''', service_data3)
        db.curs.execute('''
                           INSERT INTO Services(serviceName, cost, internetSpeed, description, provider_id)
                            VALUES (:serviceName, :cost, :internetSpeed, :description, :provider_id)
                        ''', service_data4)
        db.curs.execute('''
                           INSERT INTO Services(serviceName, cost, internetSpeed, description, provider_id)
                            VALUES (:serviceName, :cost, :internetSpeed, :description, :provider_id)
                        ''', service_data5)
        users_data1 = {
            'UserName': 'Alex1997',
            'password': 'yup11'
        }
        users_data2 = {
            'UserName': 'Nikitosik',
            'password': 'yanekit23'
        }
        users_data3 = {
            'UserName': 'Natali',
            'password': 'ntt78'
        }
        users_data4 = {
            'UserName': 'Fletttcher',
            'password': 'y313rbbb'
        }
        users_data5 = {
            'UserName': 'Igor',
            'password': 'dfkmb32'
        }
        users_data6 = {
            'UserName': 'admin',
            'password': 'admin',
            'isAdmin': 1
        }
        users_data7 = {
            'UserName': 'user',
            'password': 'user'
        }
        db.curs.execute('''
                    INSERT INTO Users(UserName, password)
                    VALUES (:UserName, :password)''', users_data1)
        db.curs.execute('''
                    INSERT INTO Users(UserName, password)
                    VALUES (:UserName, :password)''', users_data2)
        db.curs.execute('''
                    INSERT INTO Users(UserName, password)
                    VALUES (:UserName, :password)''', users_data3)
        db.curs.execute('''
                    INSERT INTO Users(UserName, password)
                    VALUES (:UserName, :password)''', users_data4)
        db.curs.execute('''
                    INSERT INTO Users(UserName, password)
                    VALUES (:UserName, :password)''', users_data5)
        db.curs.execute('''
                                    INSERT INTO Users(UserName, password, isAdmin)
                                    VALUES (:UserName, :password, :isAdmin)''', users_data6)
        db.curs.execute('''
                            INSERT INTO Users(UserName, password)
                            VALUES (:UserName, :password)''', users_data7)
        reviews_data1 = {
            'comment': 'Хороший интернет, но цена большая',
            'rating': 4,
            'user_id': 1,
            'provider_id': 1
        }
        reviews_data2 = {
            'comment': 'Хороший интернет за такую цену',
            'rating': 5,
            'user_id': 2,
            'provider_id': 2
        }
        reviews_data3 = {
            'comment': 'Скорость, конечно, низкая, но и цена не сильно большая, поэтому 4 звезды',
            'rating': 4,
            'user_id': 3,
            'provider_id': 3
        }
        reviews_data4 = {
            'comment': 'Пользуемся всем офисом и зачастую не скорость ниже заявленной',
            'rating': 3,
            'user_id': 4,
            'provider_id': 4
        }
        reviews_data5 = {
            'comment': 'Ужасный интернет, постоянные сбои и никакой скорости',
            'rating': 1,
            'user_id': 5,
            'provider_id': 5
        }
        db.curs.execute('''
                                    INSERT INTO Reviews(rating, comment, provider_id, user_id)
                                    VALUES (:rating, :comment, :provider_id, :user_id)
                                ''', reviews_data1)
        db.curs.execute('''
                                    INSERT INTO Reviews(rating, comment, provider_id, user_id)
                                    VALUES (:rating, :comment, :provider_id, :user_id)
                                ''', reviews_data2)
        db.curs.execute('''
                                    INSERT INTO Reviews(rating, comment, provider_id, user_id)
                                    VALUES (:rating, :comment, :provider_id, :user_id)
                                ''', reviews_data3)
        db.curs.execute('''
                            INSERT INTO Reviews(rating, comment, provider_id, user_id)
                            VALUES (:rating, :comment, :provider_id, :user_id)
                        ''', reviews_data4)
        db.curs.execute('''
                                    INSERT INTO Reviews(rating, comment, provider_id, user_id)
                                    VALUES (:rating, :comment, :provider_id, :user_id)
                                ''', reviews_data5)
