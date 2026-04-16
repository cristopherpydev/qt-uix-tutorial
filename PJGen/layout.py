# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pry.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from backend import *
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QTextEdit, QWidget)
dataset_classes = fetch_all_classes()
dataset_backgrounds = fetch_all_backgrounds()
dataset_races = fetch_all_races()
dataset_alignments = retrieve_all_alignments()
class Layout(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1307, 840)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(60, 40, 1191, 411))
        self.tEditChName = QLineEdit(self.groupBox)
        self.tEditChName.setObjectName(u"tEditChName")
        self.tEditChName.setGeometry(QRect(130, 60, 381, 22))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 111, 16))
        self.cbBoxRace = QComboBox(self.groupBox)
        self.cbBoxRace.setObjectName(u"cbBoxRace")
        self.cbBoxRace.setGeometry(QRect(130, 100, 211, 22))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 100, 55, 16))
        self.lvlSpinBox = QSpinBox(self.groupBox)
        self.lvlSpinBox.setObjectName(u"lvlSpinBox")
        self.lvlSpinBox.setGeometry(QRect(130, 170, 61, 31))
        self.lvlSpinBox.setMinimum(1)
        self.lvlSpinBox.setMaximum(20)
        self.lvlSpinBox.setValue(1)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 180, 81, 16))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 140, 81, 16))
        self.cbBoxClass = QComboBox(self.groupBox)
        self.cbBoxClass.setObjectName(u"cbBoxClass")
        self.cbBoxClass.setGeometry(QRect(130, 140, 211, 22))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 230, 61, 16))
        self.cbBoxAlignment = QComboBox(self.groupBox)
        self.cbBoxAlignment.setObjectName(u"cbBoxAlignment")
        self.cbBoxAlignment.setGeometry(QRect(130, 230, 211, 22))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 300, 71, 16))
        self.cbBoxBackground = QComboBox(self.groupBox)
        self.cbBoxBackground.setObjectName(u"cbBoxBackground")
        self.cbBoxBackground.setGeometry(QRect(130, 300, 211, 22))
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(620, 60, 531, 331))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(620, 30, 61, 16))
        self.rndButton = QPushButton(self.groupBox)
        self.rndButton.setObjectName(u"rndButton")
        self.rndButton.setGeometry(QRect(520, 50, 41, 41))
        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(580, 480, 121, 41))

        # configs
        self.cbBoxAlignment.addItems(dataset_alignments)
        self.cbBoxBackground.addItems(dataset_backgrounds)
        self.cbBoxClass.addItems(dataset_classes)
        self.cbBoxRace.addItems(dataset_races)



        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Personal information", None))
        self.label.setText(QCoreApplication.translate("Form", u"Character Name", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Race", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Current level", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Class", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Alignment", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Background", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Backstory", None))
        self.rndButton.setText(QCoreApplication.translate("Form", u"Rnd", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save and Print PDF", None))
    # retranslateUi

