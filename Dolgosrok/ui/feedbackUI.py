from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit, QPushButton, QVBoxLayout, QComboBox)


class feedbackUIWidget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(448, 344)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.providerCMB = QComboBox(Widget)
        self.providerCMB.setObjectName(u"providerCMB")
        self.providerCMB.setMinimumSize(QSize(221, 0))

        self.verticalLayout.addWidget(self.providerCMB)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.star1PBN = QPushButton(Widget)
        self.star1PBN.setObjectName(u"star1PBN")
        self.stars = [self.star1PBN]
        self.horizontalLayout.addWidget(self.star1PBN)

        self.star2PBN = QPushButton(Widget)
        self.star2PBN.setObjectName(u"star2PBN")
        self.stars.append(self.star2PBN)
        self.horizontalLayout.addWidget(self.star2PBN)

        self.star3PBN = QPushButton(Widget)
        self.star3PBN.setObjectName(u"star3PBN")
        self.stars.append(self.star3PBN)
        self.horizontalLayout.addWidget(self.star3PBN)

        self.star4PBN = QPushButton(Widget)
        self.star4PBN.setObjectName(u"star4PBN")
        self.stars.append(self.star4PBN)
        self.horizontalLayout.addWidget(self.star4PBN)

        self.star5PBN = QPushButton(Widget)
        self.star5PBN.setObjectName(u"star5PBN")
        self.stars.append(self.star5PBN)

        self.horizontalLayout.addWidget(self.star5PBN)



        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.hide()
        self.label.setMinimumSize(QSize(221, 0))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.feedbackPTE = QPlainTextEdit(Widget)
        self.feedbackPTE.setObjectName(u"feedbackPTE")

        self.verticalLayout.addWidget(self.feedbackPTE)

        self.sendPBN = QPushButton(Widget)
        self.sendPBN.setObjectName(u"sendPBN")

        self.verticalLayout.addWidget(self.sendPBN)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)
        self.sendPBN.clicked.connect(Widget.feedback)
        QMetaObject.connectSlotsByName(Widget)
        self.providerCMB.showPopup = Widget.combobox
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u041e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0441\u0432\u043e\u0439 \u043e\u0442\u0437\u044b\u0432", None))
        self.providerCMB.setPlaceholderText('Выберите провайдера')
        self.star1PBN.setText("")
        self.star2PBN.setText("")
        self.star3PBN.setText("")
        self.star4PBN.setText("")
        self.star5PBN.setText("")
        self.label.setText(QCoreApplication.translate("Widget", u"\u041e\u0448\u0438\u0431\u043a\u0430, \u043f\u0440\u043e\u0432\u0430\u0439\u0434\u0435\u0440 \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d", None))
        self.sendPBN.setText(QCoreApplication.translate("Widget", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u0437\u044b\u0432", None))
    # retranslateUi

