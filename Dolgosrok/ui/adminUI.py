from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import (QPushButton, QVBoxLayout)


class adminUIWidget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(455, 161)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.providerPBN = QPushButton(Widget)
        self.providerPBN.setObjectName(u"providerPBN")
        self.providerPBN.setMinimumSize(QSize(371, 0))

        self.verticalLayout.addWidget(self.providerPBN)

        self.servicePBN = QPushButton(Widget)
        self.servicePBN.setObjectName(u"servicePBN")
        self.servicePBN.setMinimumSize(QSize(431, 0))

        self.verticalLayout.addWidget(self.servicePBN)

        self.reviewPBN = QPushButton(Widget)
        self.reviewPBN.setObjectName(u"reviewPBN")
        self.reviewPBN.setMinimumSize(QSize(401, 0))

        self.verticalLayout.addWidget(self.reviewPBN)

        self.changeUserPBN = QPushButton(Widget)
        self.changeUserPBN.setObjectName(u"changeUserPBN")
        self.changeUserPBN.setMinimumSize(QSize(171, 0))

        self.verticalLayout.addWidget(self.changeUserPBN)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.servicePBN.clicked.connect(Widget.service)
        self.changeUserPBN.clicked.connect(Widget.change)
        self.providerPBN.clicked.connect(Widget.provider)
        self.reviewPBN.clicked.connect(Widget.review)
        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u0432\u0430\u0439\u0434\u0435\u0440 (\u0430\u0434\u043c\u0438\u043d)", None))
        self.providerPBN.setText('Посмотреть / редактировать информацию о провайдерах')
        self.servicePBN.setText('Посмотреть / редактировать информацию об услугах провайдеров')
        self.reviewPBN.setText('Посмотреть / редактировать информацию об отзывах')
        self.changeUserPBN.setText(QCoreApplication.translate("Widget", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
    # retranslateUi

