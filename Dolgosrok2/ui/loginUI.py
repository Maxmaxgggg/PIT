#
#
#           ФАЙЛ СОДЕРЖИТ UI ВИДЖЕТА АВТОРИЗАЦИИ
#
#


from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton, QVBoxLayout)


class loginUIWidget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(396, 221)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.userNameLED = QLineEdit(Widget)
        self.userNameLED.setObjectName(u"userNameLED")
        self.userNameLED.setMinimumSize(QSize(201, 0))
        self.verticalLayout.addWidget(self.userNameLED)

        self.passwordLED = QLineEdit(Widget)
        self.passwordLED.setObjectName(u"passwordLED")
        self.passwordLED.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.passwordLED)

        self.passwordCheckLED = QLineEdit(Widget)
        self.passwordCheckLED.setObjectName(u"passwordCheckLED")
        self.passwordCheckLED.setMinimumSize(QSize(131, 0))
        self.passwordCheckLED.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.passwordCheckLED)

        self.errorLBL = QLabel(Widget)
        self.errorLBL.setObjectName(u"errorLBL")
        self.errorLBL.setMinimumSize(QSize(261, 0))
        self.errorLBL.setMaximumSize(QSize(16777215, 20))
        self.errorLBL.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.errorLBL)

        self.loginPBN = QPushButton(Widget)
        self.loginPBN.setObjectName(u"loginPBN")
        self.loginPBN.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.loginPBN)

        self.registrationPBN = QPushButton(Widget)
        self.registrationPBN.setObjectName(u"registrationPBN")
        self.registrationPBN.setMinimumSize(QSize(91, 0))
        self.registrationPBN.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.registrationPBN)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)
        self.registrationPBN.clicked.connect(Widget.registration)
        self.loginPBN.clicked.connect(Widget.login)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.userNameLED.setInputMask("")
        self.userNameLED.setText("")
        self.userNameLED.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.passwordLED.setText("")
        self.passwordLED.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.passwordCheckLED.setPlaceholderText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.errorLBL.setText(QCoreApplication.translate("Widget", u"\u041d\u0435\u0432\u0435\u0440\u043d\u043e\u0435 \u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f/\u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.loginPBN.setText(QCoreApplication.translate("Widget", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.registrationPBN.setText(QCoreApplication.translate("Widget", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

