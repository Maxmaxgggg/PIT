import sys
from propertyContextManager import propertyContextManager
from database import path
from PySide6.QtWidgets import (QWidget,QDialog, QApplication, QComboBox, QTableView, QMessageBox)
from PySide6.QtSql import QSqlQuery, QSqlDatabase, QSqlQueryModel
from PySide6.QtCore import Qt
from ui.loginUI import loginUIWidget
from ui.userUI import userUIWidget
from ui.adminUI import adminUIWidget
from ui.editOwnersUI import editOwnersUIWidget

# Виджет для окна авторизации
class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = loginUIWidget()
        self.ui.setupUi(self)
        self.ui.errorLBL.hide()
        self.ui.passwordCheckLED.hide()

    # Слот регистрации
    def registration(self):
        # Если кнопка 'Регистрация'
        if self.ui.registrationPBN.text() == 'Регистрация':
            self.ui.errorLBL.hide()
            self.ui.errorLBL.setText('Ошибка, пароли не совпадают')
            self.ui.passwordCheckLED.show()
            self.ui.registrationPBN.setText('Отмена')
            self.ui.loginPBN.setText('Зарегистрироваться')
        # Если кнопка 'Отмена'
        else:
            self.ui.passwordCheckLED.hide()
            self.ui.errorLBL.hide()
            self.ui.errorLBL.setText('Неверное имя пользователя/пароль')
            self.ui.passwordLED.setText('')
            self.ui.passwordCheckLED.setText('')
            self.ui.registrationPBN.setText('Регистрация')
            self.ui.loginPBN.setText('Авторизоваться')

    # Слот авторизации
    def login(self):
        # Если кнопка 'Зарегистрироваться'
        if self.ui.loginPBN.text() == 'Зарегистрироваться':
            # Если пусто имя пользователя или пароль
            if self.ui.userNameLED.text() == '' or self.ui.passwordLED.text() == '':
                self.ui.errorLBL.setText('Ошибка, пустое имя пользователя/пароль')
                self.ui.errorLBL.show()
                return
            # Если пароли не совпадают
            if self.ui.passwordLED.text() != self.ui.passwordCheckLED.text():
                self.ui.errorLBL.setText('Ошибка, пароли не совпадают')
                self.ui.errorLBL.show()
            else:
                with propertyContextManager(path) as (conn, curs):
                    # Создаем таблицу users, если ее не существует
                    curs.execute('''
                        CREATE TABLE IF NOT EXISTS users(
                            id INTEGER PRIMARY KEY UNIQUE NOT NULL,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            isAdmin BOOL NOT NULL DEFAULT 0
                        )
                    ''')
                    # Ищем в таблице Users пользователя
                    curs.execute(
                        'SELECT id FROM Users WHERE username = ?',
                        (self.ui.userNameLED.text(),)
                    )
                    # Если находим пользователя, то выводим ошибку
                    if curs.fetchone():
                        self.ui.errorLBL.setText('Ошибка, такой пользователь уже существует')
                        self.ui.errorLBL.show()
                        return
                    # Если не нашли пользователя, добавляем его в базу данных
                    curs.execute(
                       'INSERT INTO Users (username, password) VALUES (?, ?)',
                       (self.ui.userNameLED.text(), self.ui.passwordLED.text())
                    )
                self.ui.errorLBL.setText('Пользователь добавлен в базу данных')
                self.ui.errorLBL.show()
                self.ui.registrationPBN.setText('Регистрация')
                self.ui.loginPBN.setText('Авторизоваться')
                self.ui.passwordLED.setText('')
                self.ui.passwordCheckLED.setText('')
                self.ui.passwordCheckLED.hide()
        # Если кнопка 'Авторизоваться'
        else:
            # Если не введено имя пользователя
            if self.ui.userNameLED.text() == '':
                self.ui.errorLBL.setText('Ошибка, пустое имя пользователя')
                self.ui.errorLBL.show()
                return
            with propertyContextManager(path) as (conn, curs):
                curs.execute('''
                    CREATE TABLE IF NOT EXISTS users(
                        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        isAdmin BOOL NOT NULL DEFAULT 0
                    )
                ''')
                # Запрашиваем пароль и статус пользователя (админ/обычный пользователь) из базы данных
                curs.execute(
                    'SELECT password, isAdmin FROM users WHERE username = ?',
                    (self.ui.userNameLED.text(),)
                )
                info = curs.fetchone()
                # Если не нашли пользователя
                if not info:
                    self.ui.errorLBL.setText('Ошибка, пользователь не найден')
                    self.ui.errorLBL.show()
                    return
                pswd, is_adm = info[0], info[1]
                # Если пароль пустой или не совпал с паролем из бд
                entered_password = self.ui.passwordLED.text()
                if pswd is None or entered_password != pswd:
                    self.ui.errorLBL.setText('Ошибка, неверное имя пользователя/пароль')
                    self.ui.errorLBL.show()
                else:
                    self.hide()
                    self.ui.userNameLED.setText('')
                    self.ui.passwordLED.setText('')
                    self.ui.errorLBL.hide()
                    # Выбираем, какой виджет запускать
                    if is_adm:
                        adminWidget.show()
                    else:
                        userWidget.show()


# Функция для получения всех записей из таблицы
def fetch_all(query: QSqlQuery):
    results = []
    while query.next():
        record = []
        for i in range(query.record().count()):
            record.append(query.value(i))
        results.append(record)
    return results


class UserWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = userUIWidget()
        self.ui.setupUi(self)
        #
        # ПОДКЛЮЧАЕМ СЛОТЫ ADDRESSCMB К СИГНАЛАМ
        #
        self.ui.addressCMB.showPopup = self.choice_addressCMB
        self.ui.addressCMB.line_edit.textEdited.connect(self.on_text_edited_addressCMB)
        #
        # ПОДКЛЮЧАЕМ СЛОТЫ OWNERCMB К СИГНАЛАМ
        #
        self.ui.ownerCMB.showPopup = self.choice_ownerCMB
        self.ui.ownerCMB.line_edit.textEdited.connect(self.on_text_edited_ownerCMB)
        #
        # ПОДКЛЮЧАЕМ СЛОТ INFOPBN К СИГНАЛУ
        #
        self.ui.infoPBN.clicked.connect(self.info)

        self.ui.findPBN.clicked.connect(self.find)

    #
    # СЛОТ INFOPBN
    #
    def info(self):
        # Если на кнопке написано 'Ввести дополнительную информацию'
        if self.ui.infoPBN.text() == 'Ввести дополнительную информацию':
            # Показываем LED-ы
            self.ui.yearLED.show()
            self.ui.phoneNumberLED.show()
            # Меняем текст на кнопке
            self.ui.infoPBN.setText('Отметить ввод дополнительной информации')
            return
        # Если на кнопке написано 'Отметить ввод дополнительной информации'
        if self.ui.infoPBN.text() == 'Отметить ввод дополнительной информации':
            # Сбрасываем текст LED-ов
            self.ui.yearLED.setText('')
            self.ui.phoneNumberLED.setText('')
            # Скрываем их
            self.ui.yearLED.hide()
            self.ui.phoneNumberLED.hide()
            # Меняем текст на кнопке
            self.ui.infoPBN.setText('Ввести дополнительную информацию')
            return

    #
    # СЛОТЫ ADDRESSCMB
    #
    def choice_addressCMB(self):
        # Удаляем текущие адреса из комбобокса
        self.ui.addressCMB.clear()
        # Запрашиваем адрес из базы данных
        query = QSqlQuery(self.db)
        query.exec('SELECT address FROM property')
        addresses = fetch_all(query)
        # Поочередно добавляем адреса в комбобокс
        for address in addresses:
            self.ui.addressCMB.addItem(address[0])
        QComboBox.showPopup(self.ui.addressCMB)

    def on_text_edited_addressCMB(self, text):
        # Устанавливаем минимальную длину, с которой открывается подсказка
        if len(text) > 1:
            # Запрашиваем адреса из базы данных
            query = QSqlQuery(f"SELECT address FROM property WHERE address LIKE '{text}%'", self.db)
            items = []
            # Поочередно добавляем адреса в массив
            while query.next():
                items.append(query.value(0))
            # Добавляем адреса в подсказку
            self.ui.addressCMB.completer.model().setStringList(items)
            self.ui.addressCMB.completer.complete()
        else:
            self.ui.addressCMB.completer.model().setStringList([])

    #
    # СЛОТЫ OWNERCMB
    #
    def choice_ownerCMB(self):
        # Удаляем текущих владельцев из комбобокса
        self.ui.ownerCMB.clear()
        # Запрашиваем имя, фамилию, отчество из базы данных
        query = QSqlQuery(self.db)
        query.exec('SELECT name, middle_name, surname FROM owners')
        # Поочередно добавляем полные имена в комбобокс
        while query.next():
            name = query.value(0)
            middle_name = query.value(1)
            surname = query.value(2)
            full_name = f"{name} {middle_name or ''} {surname}".strip()
            self.ui.ownerCMB.addItem(full_name)
        # Показываем выпадающее окошко
        QComboBox.showPopup(self.ui.ownerCMB)

    def on_text_edited_ownerCMB(self, text):
        # Устанавливаем минимальную длину, с которой открывается подсказка
        if len(text) > 1:
            # Запрашиваем имя, фамилию, отчество из базы данных
            query = QSqlQuery(self.db)
            query.prepare("""
                SELECT name, middle_name, surname 
                FROM owners 
                WHERE name LIKE :text 
                   OR middle_name LIKE :text 
                   OR surname LIKE :text
            """)
            query.bindValue(":text", f"%{text}%")
            query.exec()

            items = []
            # Все совпавшие полные имена записываем в массив
            while query.next():
                name = query.value(0)
                middle_name = query.value(1)
                surname = query.value(2)
                full_name = f"{name} {middle_name or ''} {surname}".strip()
                items.append(full_name)
            # Добавляем массив в подсказку
            self.ui.ownerCMB.completer.model().setStringList(items)
            self.ui.ownerCMB.completer.complete()
        else:
            self.ui.ownerCMB.completer.model().setStringList([])

    #
    # СЛОТ FINDPBN
    #
    def find(self):
        # Получаем id всех владельцев
        ids = []
        query = QSqlQuery(self.db)

        query.exec('''
            SELECT id FROM owners
        ''')
        while query.next():
            ids.append(query.value(0))

        # Если пользователь ввел адрес
        text = self.ui.addressCMB.line_edit.text()
        if text != '':
            ids_tmp = []
            query.prepare(f'''
                SELECT owner_id FROM property
                WHERE address = :text
            ''')
            query.bindValue(':text', text)
            # Выполнение запроса
            if query.exec():
                # Получение результатов запроса
                while query.next():
                    ids_tmp.append(query.value(0))
            else:
                print("Ошибка выполнения запроса:", query.lastError().text())
            ids = [ID for ID in ids if ID in ids_tmp]

        # Если пользователь ввел имя/фамилию/отчество
        text = self.ui.ownerCMB.line_edit.text()
        if text != '':
            ids_tmp = []
            full_name = text.split()
            if len(full_name) == 2:
                name = full_name[0]
                middle_name = None
                surname = full_name[1]
            else:
                name = full_name[0]
                middle_name = full_name[1]
                surname = full_name[2]

            if middle_name:
                query.prepare('''
                    SELECT id FROM owners
                    WHERE name = :name
                    AND middle_name = :middle_name
                    AND surname = :surname 
                ''')
                query.bindValue(':middle_name', middle_name)
            else:
                query.prepare('''
                    SELECT id FROM owners
                    WHERE name = :name
                    AND middle_name IS NULL
                    AND surname = :surname 
                ''')

            query.bindValue(':name', name)
            query.bindValue(':surname', surname)

            # Выполнение запроса
            if query.exec():
                # Получение результатов запроса
                while query.next():
                    ids_tmp.append(query.value(0))
            else:
                print("Ошибка выполнения запроса:", query.lastError().text())
            ids = [ID for ID in ids if ID in ids_tmp]

        # Если пользователь ввел номер телефона
        text = self.ui.phoneNumberLED.text()
        if text != '':
            ids_tmp = []
            query.prepare(f'''
                SELECT id FROM owners
                WHERE phoneNumber = :text
            ''')
            query.bindValue(':text', text)
            # Выполнение запроса
            if query.exec():
                # Получение результатов запроса
                while query.next():
                    ids_tmp.append(query.value(0))
            else:
                print("Ошибка выполнения запроса:", query.lastError().text())
            ids = [ID for ID in ids if ID in ids_tmp]

        # Если пользователь ввел дату рождения
        text = self.ui.yearLED.text()
        if text != '':
            ids_tmp = []
            query.prepare(f'''
                    SELECT id FROM owners
                    WHERE dateOfBirth = :text
                ''')
            query.bindValue(':text', text)
            # Выполнение запроса
            if query.exec():
                # Получение результатов запроса
                while query.next():
                    ids_tmp.append(query.value(0))
            else:
                print("Ошибка выполнения запроса:", query.lastError().text())
            ids = [ID for ID in ids if ID in ids_tmp]

        ids_str = ",".join(map(str, ids))
        query.exec(f"""
            SELECT id, name, middle_name, surname, phoneNumber, dateOfBirth
            FROM owners
            WHERE id IN ({ids_str})
        """)
        self.model = QSqlQueryModel()
        self.model.setQuery(query)
        self.model.setHeaderData(0, Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, Qt.Horizontal, 'Имя')
        self.model.setHeaderData(2, Qt.Horizontal, 'Отчество')
        self.model.setHeaderData(3, Qt.Horizontal, 'Фамилия')
        self.model.setHeaderData(4, Qt.Horizontal, 'Номер телефона')
        self.model.setHeaderData(5, Qt.Horizontal, 'Дата рождения')
        self.ui.ownerTBV.setModel(self.model)
        self.ui.ownerTBV.verticalHeader().setVisible(False)
        self.ui.ownerTBV.resizeColumnsToContents()

    #
    # СЛОТЫ ВИДЖЕТА
    #
    def show(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE', connectionName='userConnection')
        self.db.setDatabaseName(path)
        if not self.db.open():
            print('Cannot open database')
        QWidget.show(self)

    def hide(self):
        if self.db.isOpen():
            self.db.close()
        QWidget.hide(self)

    def closeEvent(self, event):
        if self.db.isOpen():
            self.db.close()


class AdminWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = adminUIWidget()
        self.ui.setupUi(self)
        #
        # ПОДКЛЮЧАЕМ СЛОТЫ ADDRESSCMB К СИГНАЛАМ
        #
        self.ui.addressCMB.showPopup = self.choice_addressCMB
        self.ui.addressCMB.line_edit.textEdited.connect(self.on_text_edited_addressCMB)
        #
        # ПОДКЛЮЧАЕМ СЛОТЫ OWNERCMB К СИГНАЛАМ
        #
        self.ui.ownerCMB.showPopup = self.choice_ownerCMB
        self.ui.ownerCMB.line_edit.textEdited.connect(self.on_text_edited_ownerCMB)
        #
        # ПОДКЛЮЧАЕМ СЛОТ INFOPBN К СИГНАЛУ INFO
        #
        self.ui.infoPBN.clicked.connect(self.info)
        #
        # ПОДКЛЮЧАЕМ СЛОТ FINDPBN К СИГНАЛУ FIND
        #
        self.ui.findPBN.clicked.connect(self.find)

        self.ui.editOwnersPBN.clicked.connect(self.editOwners)
    def editOwners(self):
        editOwnersWidget.exec()
    #
    # СЛОТ INFOPBN
    #
    def info(self):
        # Если на кнопке написано 'Ввести дополнительную информацию'
        if self.ui.infoPBN.text() == 'Ввести дополнительную информацию':
            # Показываем LED-ы
            self.ui.yearLED.show()
            self.ui.phoneNumberLED.show()
            # Меняем текст на кнопке
            self.ui.infoPBN.setText('Отметить ввод дополнительной информации')
            return
        # Если на кнопке написано 'Отметить ввод дополнительной информации'
        if self.ui.infoPBN.text() == 'Отметить ввод дополнительной информации':
            # Сбрасываем текст LED-ов
            self.ui.yearLED.setText('')
            self.ui.phoneNumberLED.setText('')
            # Скрываем их
            self.ui.yearLED.hide()
            self.ui.phoneNumberLED.hide()
            # Меняем текст на кнопке
            self.ui.infoPBN.setText('Ввести дополнительную информацию')
            return

    #
    # СЛОТЫ ADDRESSCMB
    #
    def choice_addressCMB(self):
        # Удаляем текущие адреса из комбобокса
        self.ui.addressCMB.clear()
        # Запрашиваем адрес из базы данных
        query = QSqlQuery(self.db)
        query.exec('SELECT address FROM property')
        addresses = fetch_all(query)
        # Поочередно добавляем адреса в комбобокс
        for address in addresses:
            self.ui.addressCMB.addItem(address[0])
        QComboBox.showPopup(self.ui.addressCMB)

    def on_text_edited_addressCMB(self, text):
        # Устанавливаем минимальную длину, с которой открывается подсказка
        if len(text) > 1:
            # Запрашиваем адреса из базы данных
            query = QSqlQuery(f"SELECT address FROM property WHERE address LIKE '{text}%'", self.db)
            items = []
            # Поочередно добавляем адреса в массив
            while query.next():
                items.append(query.value(0))
            # Добавляем адреса в подсказку
            self.ui.addressCMB.completer.model().setStringList(items)
            self.ui.addressCMB.completer.complete()
        else:
            self.ui.addressCMB.completer.model().setStringList([])

    #
    # СЛОТЫ OWNERCMB
    #
    def choice_ownerCMB(self):
        # Удаляем текущих владельцев из комбобокса
        self.ui.ownerCMB.clear()
        # Запрашиваем имя, фамилию, отчество из базы данных
        query = QSqlQuery(self.db)
        query.exec('SELECT name, middle_name, surname FROM owners')
        # Поочередно добавляем полные имена в комбобокс
        while query.next():
            name = query.value(0)
            middle_name = query.value(1)
            surname = query.value(2)
            full_name = f"{name} {middle_name or ''} {surname}".strip()
            self.ui.ownerCMB.addItem(full_name)
        # Показываем выпадающее окошко
        QComboBox.showPopup(self.ui.ownerCMB)

    def on_text_edited_ownerCMB(self, text):
        # Устанавливаем минимальную длину, с которой открывается подсказка
        if len(text) > 1:
            # Запрашиваем имя, фамилию, отчество из базы данных
            query = QSqlQuery(self.db)
            query.prepare("""
                SELECT name, middle_name, surname 
                FROM owners 
                WHERE name LIKE :text 
                   OR middle_name LIKE :text 
                   OR surname LIKE :text
            """)
            query.bindValue(":text", f"%{text}%")
            query.exec()

            items = []
            # Все совпавшие полные имена записываем в массив
            while query.next():
                name = query.value(0)
                middle_name = query.value(1)
                surname = query.value(2)
                full_name = f"{name} {middle_name or ''} {surname}".strip()
                items.append(full_name)
            # Добавляем массив в подсказку
            self.ui.ownerCMB.completer.model().setStringList(items)
            self.ui.ownerCMB.completer.complete()
        else:
            self.ui.ownerCMB.completer.model().setStringList([])

    #
    # СЛОТ FINDPBN
    #
    def find(self):
        # Получаем id всех владельцев
        ids = []
        query = QSqlQuery(self.db)

        query.exec('''
            SELECT id FROM owners
        ''')
        while query.next():
            ids.append(query.value(0))

        # Если пользователь ввел адрес
        text = self.ui.addressCMB.line_edit.text()
        if text != '':
            ids_tmp = []
            query.prepare(f'''
                SELECT owner_id FROM property
                WHERE address = :text
            ''')
            query.bindValue(':text', text)
            # Выполнение запроса
            if query.exec():
                # Получение результатов запроса
                while query.next():
                    ids_tmp.append(query.value(0))
            else:
                print("Ошибка выполнения запроса:", query.lastError().text())
            ids = [ID for ID in ids if ID in ids_tmp]

        # Если пользователь ввел имя/фамилию/отчество
        text = self.ui.ownerCMB.line_edit.text()
        if text != '':
            ids_tmp = []
            full_name = text.split()
            if len(full_name) == 2:
                name = full_name[0]
                middle_name = None
                surname = full_name[1]
            else:
                name = full_name[0]
                middle_name = full_name[1]
                surname = full_name[2]

            if middle_name:
                query.prepare('''
                    SELECT id FROM owners
                    WHERE name = :name
                    AND middle_name = :middle_name
                    AND surname = :surname 
                ''')
                query.bindValue(':middle_name', middle_name)
            else:
                query.prepare('''
                    SELECT id FROM owners
                    WHERE name = :name
                    AND middle_name IS NULL
                    AND surname = :surname 
                ''')

            query.bindValue(':name', name)
            query.bindValue(':surname', surname)

            # Выполнение запроса
            if query.exec():
                # Получение результатов запроса
                while query.next():
                    ids_tmp.append(query.value(0))
            else:
                print("Ошибка выполнения запроса:", query.lastError().text())
            ids = [ID for ID in ids if ID in ids_tmp]

        # Если пользователь ввел номер телефона
        text = self.ui.phoneNumberLED.text()
        if text != '':
            ids_tmp = []
            query.prepare(f'''
                SELECT id FROM owners
                WHERE phoneNumber = :text
            ''')
            query.bindValue(':text', text)
            # Выполнение запроса
            if query.exec():
                # Получение результатов запроса
                while query.next():
                    ids_tmp.append(query.value(0))
            else:
                print("Ошибка выполнения запроса:", query.lastError().text())
            ids = [ID for ID in ids if ID in ids_tmp]

        # Если пользователь ввел дату рождения
        text = self.ui.yearLED.text()
        if text != '':
            ids_tmp = []
            query.prepare(f'''
                    SELECT id FROM owners
                    WHERE dateOfBirth = :text
                ''')
            query.bindValue(':text', text)
            # Выполнение запроса
            if query.exec():
                # Получение результатов запроса
                while query.next():
                    ids_tmp.append(query.value(0))
            else:
                print("Ошибка выполнения запроса:", query.lastError().text())
            ids = [ID for ID in ids if ID in ids_tmp]

        ids_str = ",".join(map(str, ids))
        query.exec(f"""
            SELECT id, name, middle_name, surname, phoneNumber, dateOfBirth
            FROM owners
            WHERE id IN ({ids_str})
        """)
        self.model = QSqlQueryModel()
        self.model.setQuery(query)
        self.model.setHeaderData(0, Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, Qt.Horizontal, 'Имя')
        self.model.setHeaderData(2, Qt.Horizontal, 'Отчество')
        self.model.setHeaderData(3, Qt.Horizontal, 'Фамилия')
        self.model.setHeaderData(4, Qt.Horizontal, 'Номер телефона')
        self.model.setHeaderData(5, Qt.Horizontal, 'Дата рождения')
        self.ui.ownerTBV.setModel(self.model)
        self.ui.ownerTBV.verticalHeader().setVisible(False)
        self.ui.ownerTBV.resizeColumnsToContents()

    #
    # СЛОТЫ ВИДЖЕТА
    #
    def show(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE', connectionName='adminConnection')
        self.db.setDatabaseName(path)
        if not self.db.open():
            print('Cannot open database')
        QWidget.show(self)

    def hide(self):
        if self.db.isOpen():
            self.db.close()
        QWidget.hide(self)

    def closeEvent(self, event):
        if self.db.isOpen():
            self.db.close()


class EditOwnersWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = editOwnersUIWidget()
        self.ui.setupUi(self)
        self.ui.errorLBL.hide()
        self.ui.addOwnerPBN.clicked.connect(self.addOwner)
        self.ui.deleteOwnerPBN.clicked.connect(self.deleteOwner)
        self.ui.helpPBN.clicked.connect(self.show_help)
        self.mes = QMessageBox()
        self.mes.setText(f'''Для добавления собственника заполните соответствующие поля и нажмите '{self.ui.addOwnerPBN.text()}', для удаления собственников выделите их в таблице и нажмите '{self.ui.deleteOwnerPBN.text()}' ''')

    def show_help(self):
        self.mes.show()
    def exec(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE', connectionName='editOwnersConnection')
        self.db.setDatabaseName(path)
        if not self.db.open():
            print('Cannot open database')
        query = QSqlQuery(self.db)
        if not query.exec(f"""
            SELECT id, name, middle_name, surname, phoneNumber, dateOfBirth
            FROM owners
        """):
            print(query.lastError().text())
        self.model = QSqlQueryModel()
        self.model.setQuery(query)
        self.model.setHeaderData(0, Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, Qt.Horizontal, 'Имя')
        self.model.setHeaderData(2, Qt.Horizontal, 'Отчество')
        self.model.setHeaderData(3, Qt.Horizontal, 'Фамилия')
        self.model.setHeaderData(4, Qt.Horizontal, 'Номер телефона')
        self.model.setHeaderData(5, Qt.Horizontal, 'Дата рождения')
        self.ui.ownerTBV.setModel(self.model)
        self.ui.ownerTBV.setSelectionBehavior(QTableView.SelectRows)
        self.ui.ownerTBV.setSelectionMode(QTableView.MultiSelection)
        self.ui.ownerTBV.verticalHeader().setVisible(False)
        self.ui.ownerTBV.resizeColumnsToContents()
        QDialog.exec(self)

    def closeEvent(self, arg__1):
        query = QSqlQuery(self.db)
        query.exec(f"""
                    SELECT id, name, middle_name, surname, phoneNumber, dateOfBirth
                    FROM owners
        """)
        self.ui.ownerSurnameLED.setText('')
        self.ui.ownerNameLED.setText('')
        self.ui.ownerMidNameLED.setText('')
        self.ui.ownerPhoneLED.setText('')
        self.ui.dateOfBirthLED.setText('')
        self.ui.errorLBL.setText('')
        self.ui.errorLBL.hide()
        if self.db.open():
            self.db.close()

    def addOwner(self):
        name = self.ui.ownerNameLED.text()
        name = name.replace(" ", "")
        mid_name = self.ui.ownerMidNameLED.text()
        mid_name = mid_name.replace(" ", "")
        surname = self.ui.ownerSurnameLED.text()
        surname = surname.replace(" ", "")
        phoneNumber = self.ui.ownerPhoneLED.text()
        phoneNumber = phoneNumber.replace(" ", '')
        dateOfBirth = self.ui.dateOfBirthLED.text()
        dateOfBirth = dateOfBirth.replace(" ", '')

        if name == '' or surname == '':
            self.ui.errorLBL.setText('Ошибка, неверные имя/фамилия собственника')
            self.ui.errorLBL.show()
            return
        if any(char.isalpha() for char in phoneNumber):
            self.ui.errorLBL.setText('Ошибка, неверный номер телефона собственника')
            self.ui.errorLBL.show()
            return
        if any(char.isalpha() for char in dateOfBirth):
            self.ui.errorLBL.setText('Ошибка, неверная дата рождения собственника')
            self.ui.errorLBL.show()
            return
        query = QSqlQuery(self.db)
        # Параметризированный запрос на вставку данных
        query.prepare('''
            INSERT INTO owners (name, middle_name, surname, phoneNumber, dateOfBirth)
            VALUES (?, ?, ?, ?, ?);
        ''')
        query.addBindValue(name)
        query.addBindValue(mid_name)
        query.addBindValue(surname)
        query.addBindValue(phoneNumber)
        query.addBindValue(dateOfBirth)

        if query.exec():
            self.ui.errorLBL.setText('Собственник успешно добавлен')
            self.ui.ownerSurnameLED.setText('')
            self.ui.ownerNameLED.setText('')
            self.ui.ownerMidNameLED.setText('')
            self.ui.ownerPhoneLED.setText('')
            self.ui.dateOfBirthLED.setText('')
            self.ui.errorLBL.show()
        else:
            self.ui.errorLBL.setText(f'Ошибка добавления собственника: {query.lastError().text()}')
            self.ui.errorLBL.show()
        query.exec(f"""
            SELECT id, name, middle_name, surname, phoneNumber, dateOfBirth
            FROM owners
        """)
        self.model.setQuery(query)
        self.ui.ownerTBV.resizeColumnsToContents()

    def deleteOwner(self):
        indexes = self.ui.ownerTBV.selectedIndexes()
        ids_to_delete = set()
        for index in indexes:
            id = self.model.data(self.model.index(index.row(), 0))
            ids_to_delete.add(id)
        if ids_to_delete:
            ids_str = ','.join(map(str, ids_to_delete))
            query = QSqlQuery(self.db)
            if query.exec(f"DELETE FROM owners WHERE id IN ({ids_str})"):
                if len(ids_to_delete) == 1:
                    self.ui.errorLBL.setText('Собственник успешно удален')
                else:
                    self.ui.errorLBL.setText('Собственники успешно удалены')
                self.ui.errorLBL.show()
                query.exec(f"""
                    SELECT id, name, middle_name, surname, phoneNumber, dateOfBirth
                    FROM owners
                """)
                self.model.setQuery(query)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginWidget = LoginWidget()
    userWidget = UserWidget()
    adminWidget = AdminWidget()
    editOwnersWidget = EditOwnersWidget()
    loginWidget.show()
    sys.exit(app.exec())
