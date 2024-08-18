from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)

from PySide6.QtWidgets import (QPushButton, QVBoxLayout)

class userUIWidget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(375, 161)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.providerPBN = QPushButton(Widget)
        self.providerPBN.setObjectName(u"providerPBN")
        self.providerPBN.setMinimumSize(QSize(291, 0))

        self.verticalLayout.addWidget(self.providerPBN)

        self.servicePBN = QPushButton(Widget)
        self.servicePBN.setObjectName(u"servicePBN")
        self.servicePBN.setMinimumSize(QSize(351, 0))

        self.verticalLayout.addWidget(self.servicePBN)

        self.reviewPBN = QPushButton(Widget)
        self.reviewPBN.setObjectName(u"reviewPBN")
        self.reviewPBN.setMinimumSize(QSize(301, 0))

        self.verticalLayout.addWidget(self.reviewPBN)

        self.changeUserPBN = QPushButton(Widget)
        self.changeUserPBN.setObjectName(u"changeUserPBN")
        self.changeUserPBN.setMinimumSize(QSize(171, 0))

        self.verticalLayout.addWidget(self.changeUserPBN)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)
        self.changeUserPBN.clicked.connect(Widget.change)
        self.providerPBN.clicked.connect(Widget.provider)
        self.servicePBN.clicked.connect(Widget.service)
        self.reviewPBN.clicked.connect(Widget.review)
        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u0432\u0430\u0439\u0434\u0435\u0440", None))
        self.providerPBN.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u043f\u0440\u043e\u0432\u0430\u0439\u0434\u0435\u0440\u0435", None))
        self.servicePBN.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e\u0431 \u0443\u0441\u043b\u0443\u0433\u0430\u0445 \u043f\u0440\u043e\u0432\u0430\u0439\u0434\u0435\u0440\u0430", None))
        self.reviewPBN.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043e\u0442\u0437\u044b\u0432\u044b / \u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0441\u0432\u043e\u0439 \u043e\u0442\u0437\u044b\u0432", None))
        self.changeUserPBN.setText(QCoreApplication.translate("Widget", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
    # retranslateUi