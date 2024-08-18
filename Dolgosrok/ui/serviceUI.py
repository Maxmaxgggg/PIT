from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import (QHBoxLayout, QLineEdit, QPushButton, QTableView, QVBoxLayout)


class serviceUIWidget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.providerLED = QLineEdit(Widget)
        self.providerLED.setObjectName(u"providerLED")
        self.providerLED.setMinimumSize(QSize(221, 0))

        self.horizontalLayout.addWidget(self.providerLED)

        self.findPBN = QPushButton(Widget)
        self.findPBN.setObjectName(u"findPBN")
        self.findPBN.setMinimumSize(QSize(141, 29))

        self.horizontalLayout.addWidget(self.findPBN)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.serviceTBV = QTableView(Widget)
        self.serviceTBV.setObjectName(u"serviceTBV")
        self.serviceTBV.horizontalHeader().setStretchLastSection(False)
        self.serviceTBV.verticalHeader().setVisible(True)

        self.verticalLayout.addWidget(self.serviceTBV)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)
        self.findPBN.clicked.connect(Widget.search)
        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e\u0431 \u0443\u0441\u043b\u0443\u0433\u0430\u0445 \u043f\u0440\u043e\u0432\u0430\u0439\u0434\u0435\u0440\u0430", None))
        self.providerLED.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0432\u0430\u0439\u0434\u0435\u0440\u0430", None))
        self.findPBN.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0439\u0442\u0438 \u043f\u0440\u043e\u0432\u0430\u0439\u0434\u0435\u0440\u0430", None))
    # retranslateUi