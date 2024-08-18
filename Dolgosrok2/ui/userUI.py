#
#
#           ФАЙЛ СОДЕРЖИТ UI ВИДЖЕТА ПОЛЬЗОВАТЕЛЯ
#
#


from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import (QLineEdit, QPushButton, QTableView, QVBoxLayout)
from comboBox import addressComboBox, ownerComboBox


class userUIWidget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(565, 588)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addressCMB = addressComboBox(Widget)
        self.addressCMB.placeholderLED.setPlaceholderText(f'Введите адрес имущества')
        self.addressCMB.setObjectName(u"addressCMB")
        self.addressCMB.setEditable(True)
        self.verticalLayout.addWidget(self.addressCMB)
        self.ownerCMB = ownerComboBox(Widget)
        self.ownerCMB.placeholderLED.setPlaceholderText(f'Введите имя/фамилию/отчество владельца')
        self.ownerCMB.setObjectName(u"ownerCMB")
        self.verticalLayout.addWidget(self.ownerCMB)
        self.infoPBN = QPushButton(Widget)
        self.infoPBN.setObjectName(u"infoPBN")
        self.infoPBN.setMinimumSize(QSize(271, 0))
        self.verticalLayout.addWidget(self.infoPBN)
        self.phoneNumberLED = QLineEdit(Widget)
        self.phoneNumberLED.setObjectName(u"phoneNumberLED")
        self.verticalLayout.addWidget(self.phoneNumberLED)
        self.yearLED = QLineEdit(Widget)
        self.yearLED.setObjectName(u"yearLED")
        self.yearLED.setMinimumSize(QSize(271, 0))
        self.verticalLayout.addWidget(self.yearLED)
        self.findPBN = QPushButton(Widget)
        self.findPBN.setObjectName(u"findPBN")
        self.verticalLayout.addWidget(self.findPBN)
        self.ownerTBV = QTableView(Widget)
        self.ownerTBV.setObjectName(u"ownerTBV")
        self.verticalLayout.addWidget(self.ownerTBV)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(Widget)
        self.yearLED.hide()
        self.phoneNumberLED.hide()
        QMetaObject.connectSlotsByName(Widget)
    # setupUi
    def retranslateUi(self, Widget):
        Widget.setWindowTitle('Поиск собственника')
        self.addressCMB.setPlaceholderText("")
        self.infoPBN.setText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0441\u0442\u0438 \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0443\u044e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e", None))
        self.phoneNumberLED.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u0430", None))
        self.yearLED.setText("")
        self.yearLED.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u0442\u0443 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u0430", None))
        self.findPBN.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0439\u0442\u0438", None))
    # retranslateUi