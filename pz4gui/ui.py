from PyQt5.QtCore import (QCoreApplication, QMetaObject, Qt)
from PyQt5.QtWidgets import (QGridLayout, QLabel, QLineEdit, QPlainTextEdit, QPushButton, QVBoxLayout)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.FirstNumberLED = QLineEdit(Widget)
        self.FirstNumberLED.setObjectName(u"FirstNumberLED")
        self.FirstNumberLED.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.FirstNumberLED, 0, 0, 1, 1)

        self.ScndNumberLED = QLineEdit(Widget)
        self.ScndNumberLED.setObjectName(u"ScndNumberLED")
        self.ScndNumberLED.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ScndNumberLED, 0, 1, 1, 1)

        self.FirstNumberLBL = QLabel(Widget)
        self.FirstNumberLBL.setObjectName(u"FirstNumberLBL")
        self.FirstNumberLBL.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.FirstNumberLBL, 1, 0, 1, 1)

        self.ScndNumberLBL = QLabel(Widget)
        self.ScndNumberLBL.setObjectName(u"ScndNumberLBL")
        self.ScndNumberLBL.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ScndNumberLBL, 1, 1, 1, 1)

        self.CheckPBN = QPushButton(Widget)
        self.CheckPBN.setObjectName(u"CheckPBN")

        self.gridLayout.addWidget(self.CheckPBN, 2, 0, 1, 2)

        self.logPTE = QPlainTextEdit(Widget)
        self.logPTE.setObjectName(u"logPTE")
        self.logPTE.setStyleSheet(u"font: 10pt \"Courier New\";")
        self.logPTE.setReadOnly(True)

        self.gridLayout.addWidget(self.logPTE, 3, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Widget)
        self.CheckPBN.clicked.connect(Widget.check)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u0447\u0438\u0441\u0435\u043b \u043d\u0430 \u0432\u0437\u0430\u0438\u043c\u043d\u0443\u044e \u043f\u0440\u043e\u0441\u0442\u043e\u0442\u0443", None))
        self.FirstNumberLBL.setText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0435\u0440\u0432\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.ScndNumberLBL.setText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0442\u043e\u0440\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.CheckPBN.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.logPTE.setPlainText("")
    # retranslateUi
