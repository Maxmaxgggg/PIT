# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class editOwnersUIWidget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ownerTBV = QTableView(Widget)
        self.ownerTBV.setObjectName(u"ownerTBV")

        self.verticalLayout.addWidget(self.ownerTBV)

        self.ownerNameLED = QLineEdit(Widget)
        self.ownerNameLED.setObjectName(u"ownerNameLED")
        self.ownerNameLED.setMinimumSize(QSize(291, 28))

        self.verticalLayout.addWidget(self.ownerNameLED)

        self.ownerSurnameLED = QLineEdit(Widget)
        self.ownerSurnameLED.setObjectName(u"ownerSurnameLED")
        self.ownerSurnameLED.setMinimumSize(QSize(241, 0))

        self.verticalLayout.addWidget(self.ownerSurnameLED)

        self.ownerMidNameLED = QLineEdit(Widget)
        self.ownerMidNameLED.setObjectName(u"ownerMidNameLED")
        self.ownerMidNameLED.setMinimumSize(QSize(231, 0))

        self.verticalLayout.addWidget(self.ownerMidNameLED)

        self.ownerPhoneLED = QLineEdit(Widget)
        self.ownerPhoneLED.setObjectName(u"ownerPhoneLED")
        self.ownerPhoneLED.setMinimumSize(QSize(291, 0))

        self.verticalLayout.addWidget(self.ownerPhoneLED)

        self.dateOfBirthLED = QLineEdit(Widget)
        self.dateOfBirthLED.setObjectName(u"dateOfBirthLED")
        self.dateOfBirthLED.setMinimumSize(QSize(271, 0))

        self.verticalLayout.addWidget(self.dateOfBirthLED)

        self.errorLBL = QLabel(Widget)
        self.errorLBL.setObjectName(u"errorLBL")
        self.errorLBL.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.errorLBL)

        self.addOwnerPBN = QPushButton(Widget)
        self.addOwnerPBN.setObjectName(u"addOwnerPBN")

        self.verticalLayout.addWidget(self.addOwnerPBN)

        self.deleteOwnerPBN = QPushButton(Widget)
        self.deleteOwnerPBN.setObjectName(u"deleteOwnerPBN")

        self.verticalLayout.addWidget(self.deleteOwnerPBN)

        self.helpPBN = QPushButton(Widget)
        self.helpPBN.setObjectName(u"helpPBN")

        self.verticalLayout.addWidget(self.helpPBN)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u043e\u0432", None))
        self.ownerNameLED.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u0430", None))
        self.ownerSurnameLED.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0444\u0430\u043c\u0438\u043b\u0438\u044e \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u0430", None))
        self.ownerMidNameLED.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u0430", None))
        self.ownerPhoneLED.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u0430", None))
        self.dateOfBirthLED.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u0442\u0443 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u0430", None))
        self.errorLBL.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.addOwnerPBN.setText(QCoreApplication.translate("Widget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u0430", None))
        self.deleteOwnerPBN.setText('Удалить собственника/собственников')
        self.helpPBN.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

