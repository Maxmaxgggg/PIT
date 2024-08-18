import sys
import sqlite3
import configparser
from PySide6.QtWidgets import (QApplication, QWidgetAction, QWidget, QDialog, QTableView,
                               QStyledItemDelegate, QStyleOptionViewItem, QStyle, QMenu,
                               QLabel, QAbstractItemView, QComboBox)
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlQueryModel
from PySide6.QtCore import Qt, QPoint, QSortFilterProxyModel
from PySide6.QtGui import QIcon, QFontMetrics

from ui.loginUI import loginUIWidget
from ui.feedbackUI import feedbackUIWidget
from ui.userUI import userUIWidget
from ui.providerUI import providerUIWidget
from ui.serviceUI import serviceUIWidget
from ui.reviewUI import reviewUIWidget
from ui.adminUI import adminUIWidget

# Переменные для хранения данных о пользователе
user = []
admn = []

# И о названиях подключений к бд
p_con = 'providerConnection'
s_con = 'serviceConnection'
r_con = 'reviewConnection'

# Читаем путь до бд из конфиг-файла
config = configparser.ConfigParser()
config.read('path.ini')
path = config.get('DEFAULT', 'path')


class EditableSqlQueryModel1(QSqlQueryModel):
    # Т.к. соединение имеет нестандартное название, необходимо передавать объект бд в качестве аргумента
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db

    # Метод установки данных в элемент модели
    def setData(self, index, value, role=Qt.EditRole) -> bool:
        if index.isValid() and role == Qt.EditRole:
            if not admn[0]:
                return False
            # Получаем имя столбца по индексу
            column_name = self.record().fieldName(index.column())
            # Получаем значение ID строки
            id_value = self.data(self.index(index.row(), 0))  # Предполагается, что первый столбец - ID
            # Готовим SQL запрос для обновления значения
            query = QSqlQuery(self.db)
            # Если пытаемся изменить имя провайдера, то необходимо проверить, есть ли она в бд
            if column_name == 'providerName':
                # Подготовка запроса для проверки существования провайдера
                check_query = QSqlQuery(self.db)
                check_query.prepare("SELECT id FROM Providers WHERE providerName = ?")
                check_query.addBindValue(value)
                if not check_query.exec():
                    print("Ошибка при выполнении запроса:", check_query.lastError().text())
                    return False

                if check_query.next():
                    # Если провайдер существует, обновляем provider_id в таблице Services
                    provider_id = check_query.value(0)  # Получаем id провайдера из результата запроса
                    update_query = QSqlQuery(self.db)
                    update_query.prepare("UPDATE Services SET provider_id = ? WHERE id = ?")
                    update_query.addBindValue(provider_id)
                    update_query.addBindValue(id_value)
                    if not update_query.exec():
                        print("Ошибка при обновлении данных:", update_query.lastError().text())
                        return False
                    self.refresh()
                    return True
                else:
                    # Если провайдер не существует, отменяем изменения
                    return False
            query.prepare(f"UPDATE Services SET {column_name} = ? WHERE id = ?")
            query.addBindValue(value)
            query.addBindValue(id_value)
            if not query.exec():
                print("Ошибка при обновлении данных:", query.lastError().text())
                return False
            self.refresh()
            return True
        return False

    def flags(self, index):
        # Включаем флаги Qt.ItemIsEditable и Qt.ItemIsEnabled для всех ячеек
        flags = super().flags(index)
        if index.isValid():
            flags |= Qt.ItemIsEditable
        return flags

    # Метод обновления элементов таблицы
    def refresh(self) -> None:
        query = QSqlQuery(self.db)
        query.exec(self.query().executedQuery())
        self.setQuery(query)


class EditableSqlQueryModel2(QSqlQueryModel):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db

    def setData(self, index, value, role=Qt.EditRole) -> bool:
        if index.isValid() and role == Qt.EditRole:
            if not admn[0]:
                return False
            # Получаем имя столбца по индексу
            column_name = self.record().fieldName(index.column())
            # Получаем значение ID строки
            id_value = self.data(self.index(index.row(), 0))  # Предполагается, что первый столбец - ID
            # Готовим SQL запрос для обновления значения
            query = QSqlQuery(self.db)
            if column_name == 'providerName':
                # Подготовка запроса для проверки существования провайдера
                check_query = QSqlQuery(self.db)
                check_query.prepare("SELECT id FROM Providers WHERE providerName = ?")
                check_query.addBindValue(value)
                if not check_query.exec():
                    print("Ошибка при выполнении запроса:", check_query.lastError().text())
                    return False
                if check_query.next():
                    # Если провайдер существует, обновляем provider_id в таблице Services
                    provider_id = check_query.value(0)  # Получаем id провайдера из результата запроса
                    update_query = QSqlQuery(self.db)
                    update_query.prepare("UPDATE Reviews SET provider_id = ? WHERE id = ?")
                    update_query.addBindValue(provider_id)
                    update_query.addBindValue(id_value)
                    if not update_query.exec():
                        print("Ошибка при обновлении данных:", update_query.lastError().text())
                        return False
                    self.refresh()
                    return True
                else:
                    # Если провайдер не существует, отменяем изменения
                    return False
            if column_name == 'userName':
                # Подготовка запроса для проверки существования провайдера
                check_query = QSqlQuery(self.db)
                check_query.prepare("SELECT id FROM Users WHERE userName = ?")
                check_query.addBindValue(value)
                if not check_query.exec():
                    print("Ошибка при выполнении запроса:", check_query.lastError().text())
                    return False
                if check_query.next():
                    # Если провайдер существует, обновляем provider_id в таблице Services
                    provider_id = check_query.value(0)  # Получаем id провайдера из результата запроса
                    update_query = QSqlQuery(self.db)
                    update_query.prepare("UPDATE Reviews SET user_id = ? WHERE id = ?")
                    update_query.addBindValue(provider_id)
                    update_query.addBindValue(id_value)
                    if not update_query.exec():
                        print("Ошибка при обновлении данных:", update_query.lastError().text())
                        return False
                    self.refresh()
                    return True
                else:
                    # Если провайдер не существует, отменяем изменения
                    return False
            query.prepare(f"UPDATE Reviews SET {column_name} = ? WHERE id = ?")
            query.addBindValue(value)
            query.addBindValue(id_value)
            if not query.exec():
                print("Ошибка при обновлении данных:", query.lastError().text())
                return False
            self.refresh()
            return True
        return False

    def flags(self, index):
        # Включаем флаги Qt.ItemIsEditable и Qt.ItemIsEnabled для всех ячеек
        flags = super().flags(index)
        if index.isValid():
            flags |= Qt.ItemIsEditable
        return flags

    def refresh(self) -> None:
        query = QSqlQuery(self.db)
        query.exec(self.query().executedQuery())
        self.setQuery(query)


# Делегат для обычного пользователя
class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        # Переопределяем метод создания редактора, чтобы он не создавал редактор
        return None

    def setEditorData(self, editor, index):
        # Переопределяем метод установки данных в редактор, чтобы не устанавливать данные
        pass

    def setModelData(self, editor, model, index):
        # Переопределяем метод установки данных в модель, чтобы не передавать данные из редактора в модель
        pass


# Делегат для смещения текста в таблице
class TextWrapDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(TextWrapDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        options = QStyleOptionViewItem(option)
        self.initStyleOption(options, index)

        painter.save()

        text = options.text
        options.text = ""
        options.widget.style().drawControl(QStyle.CE_ItemViewItem, options, painter)

        text_rect = options.rect
        text_rect.setTop(text_rect.top() + 5)
        text_rect.setLeft(text_rect.left() + 5)
        text_rect.setRight(text_rect.right() - 5)
        text_rect.setBottom(text_rect.bottom() - 5)

        painter.drawText(text_rect, Qt.TextWordWrap, text)

        painter.restore()

    def sizeHint(self, option, index):
        options = QStyleOptionViewItem(option)
        self.initStyleOption(options, index)

        metrics = QFontMetrics(options.font)
        text = options.text
        text_rect = metrics.boundingRect(0, 0, option.rect.width(), 0, Qt.TextWordWrap, text)

        return text_rect.size()


# Менеджер контекста для работы с бд
class ContextManager:
    def __init__(self, pth: str):
        self.path = pth

    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        self.conn.execute('PRAGMA foreign_keys=ON;')
        self.curs = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


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
                with ContextManager(path) as db:
                    # Создаем таблицу Users, если ее не существует
                    db.curs.execute('''
                        CREATE TABLE IF NOT EXISTS Users(
                            id INTEGER PRIMARY KEY,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            isAdmin BIT NOT NULL DEFAULT 0
                        )
                    ''')
                    # Ищем в таблице Users пользователя
                    db.curs.execute(
                        'SELECT id FROM Users WHERE username = ?',
                        (self.ui.userNameLED.text(),)
                    )
                    # Если находим пользователя, то выводим ошибку
                    if db.curs.fetchone():
                        self.ui.errorLBL.setText('Ошибка, такой пользователь уже существует')
                        self.ui.errorLBL.show()
                        return
                    # Если не нашли пользователя, добавляем его в базу данных
                    db.curs.execute(
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
            with ContextManager(path) as db:
                db.curs.execute('''
                    CREATE TABLE IF NOT EXISTS Users(
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        isAdmin BIT NOT NULL DEFAULT 0
                    )
                ''')
                # Запрашиваем пароль и статус пользователя(админ/обычный пользователь) из базы данных
                db.curs.execute(
                    'SELECT password, isAdmin FROM Users WHERE username = ?',
                    (self.ui.userNameLED.text(),)
                )
                info = db.curs.fetchone()
                if not info:
                    self.ui.errorLBL.setText('Ошибка, пользователь не найден')
                    self.ui.errorLBL.show()
                    return
                pswd, is_adm = info[0], info[1]
                # Если пароль пустой
                if pswd is None:
                    self.ui.errorLBL.setText('Ошибка, неверное имя пользователя/пароль')
                    self.ui.errorLBL.show()
                else:
                    # Сравниваем пароль, введенный пользователем с паролем в базе данных
                    entered_password = self.ui.passwordLED.text()
                    # Если пароли совпали
                    if pswd == entered_password:
                        self.hide()
                        user.append(self.ui.userNameLED.text())
                        admn.append(is_adm)
                        self.ui.userNameLED.setText('')
                        self.ui.passwordLED.setText('')
                        self.ui.errorLBL.hide()
                        # Выбираем, какой виджет запускать
                        if is_adm:
                            adminWidget.show()
                        else:
                            userWidget.show()
                    # Если пароли не совпали
                    else:
                        self.ui.errorLBL.setText('Ошибка, неверное имя пользователя/пароль')
                        self.ui.errorLBL.show()


# Виджет для окна пользователя
class UserWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.readOnlyDelegate = ReadOnlyDelegate()
        self.ui = userUIWidget()
        self.ui.setupUi(self)

    # Слот смены пользователя
    def change(self) -> None:
        # Удаляем текущее имя пользователяGG
        user.pop()
        admn.pop()
        self.hide()
        loginWidget.show()

    # Слот просмотра информации о провайдерах
    @staticmethod
    def provider() -> None:
        providerWidget.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        providerWidget.ui.providerTBV.setEditTriggers(QTableView.NoEditTriggers)
        providerWidget.exec()

    # Слот просмотра услуг провайдеров
    def service(self) -> None:
        serviceWidget.ui.serviceTBV.setItemDelegate(self.readOnlyDelegate)
        serviceWidget.exec()

    # Слот просмотра отзывов о провайдерах
    def review(self) -> None:
        reviewWidget.ui.reviewTBV.setItemDelegate(self.readOnlyDelegate)
        reviewWidget.exec()


# Виджет для окна админа
class AdminWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = adminUIWidget()
        self.ui.setupUi(self)

    def change(self) -> None:
        # Удаляем текущее имя пользователяGG
        admn.pop()
        user.pop()
        self.hide()
        loginWidget.show()

    @staticmethod
    def provider() -> None:
        providerWidget.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        providerWidget.ui.providerTBV.setEditTriggers(QTableView.DoubleClicked | QTableView.SelectedClicked)
        providerWidget.exec()

    @staticmethod
    def service() -> None:
        serviceWidget.ui.serviceTBV.setItemDelegate(QStyledItemDelegate(serviceWidget.ui.serviceTBV))
        serviceWidget.ui.serviceTBV.setEditTriggers(QTableView.DoubleClicked | QTableView.SelectedClicked)
        serviceWidget.ui.serviceTBV.setSelectionBehavior(QAbstractItemView.SelectRows)
        serviceWidget.ui.serviceTBV.setSelectionMode(QAbstractItemView.SingleSelection)
        serviceWidget.exec()

    @staticmethod
    def review() -> None:
        reviewWidget.ui.reviewTBV.setItemDelegate(QStyledItemDelegate(reviewWidget.ui.reviewTBV))
        reviewWidget.ui.reviewTBV.setEditTriggers(QTableView.DoubleClicked | QTableView.SelectedClicked)
        reviewWidget.ui.reviewTBV.setSelectionBehavior(QAbstractItemView.SelectRows)
        reviewWidget.ui.reviewTBV.setSelectionMode(QAbstractItemView.SingleSelection)
        reviewWidget.exec()


class ProviderWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = providerUIWidget()
        self.ui.setupUi(self)
        # Подключаемся к базе данных
        self.db = QSqlDatabase.addDatabase('QSQLITE', connectionName=p_con)
        self.db.setDatabaseName(path)
        if not self.db.open():
            print('Cannot open database')

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('Providers')
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, Qt.Horizontal, 'Название')
        self.model.setHeaderData(2, Qt.Horizontal, 'Число пользователей')
        self.model.setHeaderData(3, Qt.Horizontal, 'Адрес')
        self.model.setHeaderData(4, Qt.Horizontal, 'Номер телефона')
        self.model.setHeaderData(5, Qt.Horizontal, 'Почтовый ящик')
        self.model.setHeaderData(6, Qt.Horizontal, 'Вебсайт')
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.ui.providerTBV.setModel(self.proxy_model)
        self.ui.providerTBV.verticalHeader().setVisible(False)
        # Устанавливаем политику контекстного меню на CustomContextMenu
        self.ui.providerTBV.setContextMenuPolicy(Qt.CustomContextMenu)

        # Связываем сигнал customContextMenuRequested с методом open_menu
        self.ui.providerTBV.customContextMenuRequested.connect(self.open_menu)
        # Соединяем сигнал клика по заголовку столбца со слотом для сортировки
        self.ui.providerTBV.horizontalHeader().sectionClicked.connect(self.sort_column)
        self.ui.providerTBV.horizontalHeader().sectionResized.connect(self.update_row_heights)
        self.ui.providerTBV.resizeColumnsToContents()

        # Добавляем переменную для отслеживания текущего порядка сортировки
        self.current_sort_order = Qt.AscendingOrder

    def open_menu(self, position: QPoint) -> None:
        if admn[0]:
            indexes = self.ui.providerTBV.selectedIndexes()
            if indexes:
                index = self.ui.providerTBV.indexAt(position)
                if not index.column():
                    menu = QMenu()

                    # Создаем QWidgetAction для пункта "Удалить"
                    delete_action = QWidgetAction(self)
                    delete_label = QLabel("Удалить", self)
                    delete_label.setAlignment(Qt.AlignCenter)
                    delete_action.setDefaultWidget(delete_label)

                    # Соединяем сигнал triggered с удалением строки
                    delete_action.triggered.connect(lambda: self.delete_row(indexes[0]))

                    # Добавляем действие в меню
                    menu.addAction(delete_action)

                    action = menu.exec(self.ui.providerTBV.viewport().mapToGlobal(position))
                    if action == delete_action:
                        index = indexes[0]
                        id = self.model.data(index)
                        self.delete_row(id)

    def delete_row(self, id) -> None:
        if admn[0]:
            query = QSqlQuery(self.db)
            query.prepare("DELETE FROM Providers WHERE id = ?")
            query.addBindValue(id)
            query.exec()
            query.prepare("DELETE FROM Services WHERE provider_id = ?")
            query.addBindValue(id)
            query.exec()
            serviceWidget.model.refresh()
            query.prepare("DELETE FROM Reviews WHERE provider_id = ?")
            query.addBindValue(id)
            query.exec()
            reviewWidget.model.refresh()
            self.model.select()

    def update_row_heights(self):
        for row in range(self.model.rowCount()):
            self.ui.providerTBV.resizeRowToContents(row)

    # Слот поиска провайдера
    def search(self):
        provider = self.ui.providerLED.text()
        # Получаем текст из поля поиска
        # Формируем строку фильтрации для модели
        filter_str = f"providerName LIKE '%{provider}%'"
        self.model.setFilter(filter_str)
        self.model.select()

    # Метод сортировки столбца при нажатии на название
    def sort_column(self, logical_index):
        # Определяем номер фактического столбца по его логическому индексу
        column_index = self.ui.providerTBV.horizontalHeader().logicalIndex(logical_index)
        self.current_sort_order = Qt.DescendingOrder if self.current_sort_order == Qt.AscendingOrder else Qt.AscendingOrder
        self.proxy_model.sort(column_index, self.current_sort_order)

    def closeEvent(self, arg__1):
        self.ui.providerLED.setText('')
        self.search()

    def __del__(self):
        if self.db and self.db.isOpen():
            self.db.close()


class ServiceWidget(QDialog):
    def __init__(self, parent=None):
        self.column_names = {
            0: "s.id",
            1: "s.serviceName",
            2: "s.cost",
            3: "s.internetSpeed",
            4: "s.description",
            5: "p.providerName"
        }
        super().__init__(parent)
        self.ui = serviceUIWidget()
        self.ui.setupUi(self)
        self.db = QSqlDatabase.addDatabase('QSQLITE', connectionName=s_con)
        self.db.setDatabaseName(path)
        if not self.db.open():
            print('Cannot open database')

        query = QSqlQuery(self.db)

        self.query_base = """
                    SELECT s.id, s.serviceName, s.cost, s.internetSpeed, s.description, p.providerName
                    FROM Services s
                    INNER JOIN Providers p ON s.provider_id = p.id
                """
        query.prepare(self.query_base)
        query.exec()
        if not query.exec():
            print(query.lastError())
        # Создание модели данных
        self.model = EditableSqlQueryModel1(self.db)
        self.model.setQuery(query)
        self.model.setHeaderData(0, Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, Qt.Horizontal, 'Название услуги')
        self.model.setHeaderData(2, Qt.Horizontal, 'Цена')
        self.model.setHeaderData(3, Qt.Horizontal, 'Скорость интернета')
        self.model.setHeaderData(4, Qt.Horizontal, 'Описание')
        self.model.setHeaderData(5, Qt.Horizontal, 'Название провайдера')

        # Прокси модель для фильтрации
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)

        self.ui.serviceTBV.setModel(self.proxy_model)
        self.ui.serviceTBV.verticalHeader().setVisible(False)
        # Установите политику контекстного меню на CustomContextMenu
        self.ui.serviceTBV.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.serviceTBV.customContextMenuRequested.connect(self.open_menu)

        # Соединяем сигнал клика по заголовку столбца со слотом для сортировки
        self.ui.serviceTBV.horizontalHeader().sectionClicked.connect(self.sort_column)
        self.ui.serviceTBV.setEditTriggers(QTableView.NoEditTriggers)
        self.ui.serviceTBV.horizontalHeader().sectionResized.connect(self.update_row_heights)
        self.ui.serviceTBV.resizeColumnsToContents()
        # Добавляем переменные для отслеживания текущего столбца сортировки
        self.current_sort_column = None
        self.current_sort_order = Qt.AscendingOrder

    def exec(self):
        if not self.db.isOpen():
            self.db = QSqlDatabase.addDatabase('QSQLITE', connectionName=s_con)
            self.db.setDatabaseName(path)
        super().exec()

    def open_menu(self, position: QPoint):
        if admn[0]:
            indexes = self.ui.serviceTBV.selectedIndexes()
            if indexes:
                index = self.ui.serviceTBV.indexAt(position)
                if not index.column():
                    menu = QMenu()

                    # Создаем QWidgetAction для пункта "Удалить"
                    delete_action = QWidgetAction(self)
                    delete_label = QLabel("Удалить", self)
                    delete_label.setAlignment(Qt.AlignCenter)
                    delete_action.setDefaultWidget(delete_label)

                    # Соединяем сигнал triggered с удалением строки
                    delete_action.triggered.connect(lambda: self.delete_row(indexes[0]))

                    # Добавляем действие в меню
                    menu.addAction(delete_action)

                    action = menu.exec(self.ui.serviceTBV.viewport().mapToGlobal(position))
                    if action == delete_action:
                        index = indexes[0]
                        id = self.model.data(index)
                        self.delete_row(id)

    def delete_row(self, id):
        if admn[0]:
            query = QSqlQuery(self.db)
            query.prepare("DELETE FROM Services WHERE id = ?")
            query.addBindValue(id)
            query.exec()
            self.update_model()

    def update_row_heights(self):
        for row in range(self.model.rowCount()):
            self.ui.serviceTBV.resizeRowToContents(row)

    def update_model(self, provider_filter=None, sort_column=None, sort_order=Qt.AscendingOrder):
        if not self.db.isOpen():
            print('Fucking fuck')
        query = QSqlQuery(self.db)
        query_string = self.query_base
        if provider_filter:
            query_string += " WHERE p.providerName LIKE :providerName"
        # Если сортируем колонки
        if sort_column is not None:
            order = "ASC" if sort_order == Qt.AscendingOrder else "DESC"
            query_string += f" ORDER BY {sort_column} {order}"
        query.prepare(query_string)
        # Если ищем
        if provider_filter:
            query.bindValue(":providerName", f"%{provider_filter}%")
        query.exec()
        if not query.exec():
            print(query.lastError().text())

        self.model.setQuery(query)
        self.model.setHeaderData(0, Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, Qt.Horizontal, 'Название услуги')
        self.model.setHeaderData(2, Qt.Horizontal, 'Цена')
        self.model.setHeaderData(3, Qt.Horizontal, 'Скорость интернета')
        self.model.setHeaderData(4, Qt.Horizontal, 'Описание')
        self.model.setHeaderData(5, Qt.Horizontal, 'Название провайдера')

    def search(self):
        provider_name = self.ui.providerLED.text()
        self.update_model(provider_name)

    # Метод сортировки столбца при нажатии на название
    def sort_column(self, logical_index):
        column_name = self.column_names[logical_index]
        text = None
        if self.ui.providerLED.text() != '':
            text = self.ui.providerLED.text()
        self.current_sort_order = Qt.DescendingOrder if self.current_sort_order == Qt.AscendingOrder else Qt.AscendingOrder
        self.update_model(provider_filter=text, sort_column=column_name, sort_order=self.current_sort_order)

    def closeEvent(self, arg__1):
        self.ui.providerLED.setText('')
        self.search()

    def __del__(self):
        if self.db and self.db.isOpen():
            self.db.close()


class ReviewWidget(QDialog):
    def __init__(self, parent=None):
        self.column_names = {
            0: "r.id",
            1: "r.rating",
            2: "r.comment",
            3: "r.dateTime",
            4: "p.providerName",
            5: "u.userName"
        }
        super().__init__(parent)
        self.ui = reviewUIWidget()
        self.ui.setupUi(self)
        self.db = QSqlDatabase.addDatabase('QSQLITE', connectionName='reviewConnection')
        self.db.setDatabaseName(path)
        if not self.db.open():
            print('Cannot open database')

        query = QSqlQuery(self.db)

        self.query_base = """
                    SELECT r.id, r.rating, r.comment, r.dateTime, p.providerName, u.userName
                    FROM Reviews r
                    INNER JOIN Providers p ON r.provider_id = p.id
                    INNER JOIN Users u ON r.user_id = u.id
                """
        query.prepare(self.query_base)
        query.exec()
        # Создание модели данных
        self.model = EditableSqlQueryModel2(self.db)
        self.model.setQuery(query)
        self.model.setHeaderData(0, Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, Qt.Horizontal, 'Оценка')
        self.model.setHeaderData(2, Qt.Horizontal, 'Комментарий')
        self.model.setHeaderData(3, Qt.Horizontal, 'Дата отзыва')
        self.model.setHeaderData(4, Qt.Horizontal, 'Название провайдера')
        self.model.setHeaderData(5, Qt.Horizontal, 'Имя пользователя')
        self.ui.reviewTBV.setModel(self.model)
        self.ui.reviewTBV.verticalHeader().setVisible(False)
        # Установите политику контекстного меню на CustomContextMenu
        self.ui.reviewTBV.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.reviewTBV.customContextMenuRequested.connect(self.open_menu)

        # Соединяем сигнал клика по заголовку столбца со слотом для сортировки
        self.ui.reviewTBV.horizontalHeader().sectionClicked.connect(self.sort_column)
        self.ui.reviewTBV.horizontalHeader().sectionResized.connect(self.update_row_heights)
        self.ui.reviewTBV.resizeColumnsToContents()
        # Добавляем переменные для отслеживания текущего столбца сортировки
        self.current_sort_column = None
        self.current_sort_order = Qt.AscendingOrder

    def open_menu(self, position: QPoint):
        if admn[0]:
            indexes = self.ui.reviewTBV.selectedIndexes()
            if indexes:
                index = self.ui.reviewTBV.indexAt(position)
                if not index.column():
                    menu = QMenu()

                    # Создаем QWidgetAction для пункта "Удалить"
                    delete_action = QWidgetAction(self)
                    delete_label = QLabel("Удалить", self)
                    delete_label.setAlignment(Qt.AlignCenter)
                    delete_action.setDefaultWidget(delete_label)

                    # Соединяем сигнал triggered с удалением строки
                    delete_action.triggered.connect(lambda: self.delete_row(indexes[0]))

                    # Добавляем действие в меню
                    menu.addAction(delete_action)

                    action = menu.exec(self.ui.reviewTBV.viewport().mapToGlobal(position))
                    if action == delete_action:
                        index = indexes[0]
                        id = self.model.data(index)
                        self.delete_row(id)

    def delete_row(self, id):
        if admn[0]:
            query = QSqlQuery(self.db)
            query.prepare("DELETE FROM Reviews WHERE id = ?")
            query.addBindValue(id)
            query.exec()
            self.update_model()

    def update_row_heights(self):
        for row in range(self.model.rowCount()):
            self.ui.reviewTBV.resizeRowToContents(row)

    def update_model(self, provider_filter=None, sort_column=None, sort_order=Qt.AscendingOrder):
        query = QSqlQuery(self.db)
        query_string = self.query_base
        if provider_filter:
            query_string += "   WHERE p.providerName LIKE :providerName"
        # Если сортируем колонки
        if sort_column is not None:
            order = "ASC" if sort_order == Qt.AscendingOrder else "DESC"
            query_string += f" ORDER BY {sort_column} {order}"
        query.prepare(query_string)
        # Если ищем
        if provider_filter:
            query.bindValue(":providerName", f"%{provider_filter}%")
        query.exec()
        self.model.setQuery(query)
        self.model.setHeaderData(0, Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, Qt.Horizontal, 'Оценка')
        self.model.setHeaderData(2, Qt.Horizontal, 'Комментарий')
        self.model.setHeaderData(3, Qt.Horizontal, 'Дата отзыва')
        self.model.setHeaderData(4, Qt.Horizontal, 'Название провайдера')
        self.model.setHeaderData(5, Qt.Horizontal, 'Имя пользователя')

    def search(self):
        provider_name = self.ui.providerLED.text()
        self.update_model(provider_name)

    # Метод сортировки столбца при нажатии на название
    def sort_column(self, logical_index):
        column_name = self.column_names[logical_index]
        text = None
        if self.ui.providerLED.text() != '':
            text = self.ui.providerLED.text()
        self.current_sort_order = Qt.DescendingOrder if self.current_sort_order == Qt.AscendingOrder else Qt.AscendingOrder
        self.update_model(provider_filter=text, sort_column=column_name, sort_order=self.current_sort_order)

    @staticmethod
    def feedback():
        feedbackWidget.exec()

    def closeEvent(self, arg__1):
        self.ui.providerLED.setText('')
        self.search()

    def __del__(self):
        if self.db and self.db.isOpen():
            self.db.close()


# Виджет для создания отзыва
class FeedbackWidget(QDialog):
    def __init__(self, parent=None):

        self.q = 0
        super().__init__(parent)
        self.ui = feedbackUIWidget()
        self.ui.setupUi(self)

        for obj in self.ui.stars:
            obj.clicked.connect(self.star_clicked)
            obj.setIcon(QIcon('ui/star-empty.png'))
            obj.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0); /* Полностью прозрачный фон */
                border: none;  /* Убираем границы */
                color: black;  /* Цвет текста */
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0); /* Полупрозрачный фон при наведении */
            }
            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 0); /* Полупрозрачный фон при нажатии */
            }
        """)

    def star_clicked(self):
        self.q = 0
        star = self.sender()
        index = self.ui.stars.index(star)
        # Помечаем все звезды до текущей как заполненные
        for i in range(index + 1):
            self.ui.stars[i].setIcon(QIcon('ui/star.png'))
            self.q += 1
        # Помечаем все звезды после текущей как пустые
        for i in range(index + 1, len(self.ui.stars)):
            self.ui.stars[i].setIcon(QIcon('ui/star-empty.png'))

    def combobox(self):
        self.ui.providerCMB.clear()
        with ContextManager(path) as db:
            db.curs.execute('SELECT providerName FROM Providers')
            providers = db.curs.fetchall()
            # Добавление всех providerName в QComboBox
            for provider in providers:
                self.ui.providerCMB.addItem(provider[0])
        QComboBox.showPopup(self.ui.providerCMB)

    def feedback(self):
        pname = self.ui.providerCMB.currentText()
        if pname == '':
            self.ui.label.setText('Ошибка, выберите провайдера')
            self.ui.label.show()
            return
        if self.q == 0:
            self.ui.label.setText('Ошибка, поставьте оценку')
            self.ui.label.show()
            return
        comment = self.ui.feedbackPTE.toPlainText()
        if comment == '':
            self.q = 0
            self.ui.label.setText('Ошибка, нельзя оставить пустой отзыв')
            self.ui.label.show()
            return
        with ContextManager(path) as db:
            db.curs.execute('''
                        SELECT id FROM Providers
                        WHERE providerName LIKE ?
                    ''', (pname,))
            p_id = db.curs.fetchone()
            if not p_id:
                self.ui.label.setText('Ошибка, провайдер не найден')
                self.ui.label.show()
                return
            db.curs.execute(f'''
            SELECT id FROM Users
            WHERE userName LIKE ?
            ''', (user[0],))
            u_id = db.curs.fetchone()
            db.curs.execute("""
                INSERT INTO Reviews (rating, comment, provider_id, user_id)
                VALUES (?, ?, ?, ?)
            """, (self.q, comment, p_id[0], u_id[0]))
            self.ui.label.setText('Отзыв успешно добавлен')
            self.ui.label.show()
            self.ui.feedbackPTE.setPlainText('')
            self.ui.providerCMB.setCurrentIndex(-1)
            for i in range(len(self.ui.stars)):
                self.ui.stars[i].setIcon(QIcon('ui/star-empty.png'))

    def closeEvent(self, arg__1):
        reviewWidget.model.refresh()
        self.q = 0
        for i in range(len(self.ui.stars)):
            self.ui.stars[i].setIcon(QIcon('ui/star-empty.png'))
        self.ui.providerCMB.setCurrentIndex(-1)
        self.ui.label.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создаем виджеты
    loginWidget = LoginWidget()
    userWidget = UserWidget()
    adminWidget = AdminWidget()
    providerWidget = ProviderWidget()
    serviceWidget = ServiceWidget()
    reviewWidget = ReviewWidget()
    feedbackWidget = FeedbackWidget()

    # Отображаем виджет авторизации
    loginWidget.show()
    sys.exit(app.exec())
