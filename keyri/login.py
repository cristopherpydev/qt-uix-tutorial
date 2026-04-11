# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import csv
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget,QMainWindow)

from dashboard import Dashboard

class Login(object): 
    def setupUi(self, mainWindow):
        #========================== WINDOW CONFIG =======================#

        self.mainWindow = mainWindow

        #========================== WINDOW 2 CONFIG =======================#

        self.window2 = QMainWindow()
        self.ui2 = Dashboard()
        self.ui2.setupUi(self.window2, self.mainWindow)

        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(511, 303)
        self.lnEdit_usuario = QLineEdit(mainWindow)
        self.lnEdit_usuario.setObjectName(u"lnEdit_usuario")
        self.lnEdit_usuario.setGeometry(QRect(140, 80, 211, 22))
        self.lnEdit_usuario.setMaxLength(16)
        self.lbl_usuario = QLabel(mainWindow)
        self.lbl_usuario.setObjectName(u"lbl_usuario")
        self.lbl_usuario.setGeometry(QRect(140, 60, 55, 16))
        self.lbl_contrasenia = QLabel(mainWindow)
        self.lbl_contrasenia.setObjectName(u"lbl_contrasenia")
        self.lbl_contrasenia.setGeometry(QRect(140, 130, 71, 16))
        self.lnEdit_contrasenia = QLineEdit(mainWindow)
        self.lnEdit_contrasenia.setObjectName(u"lnEdit_contrasenia")
        self.lnEdit_contrasenia.setGeometry(QRect(140, 150, 211, 22))
        self.lnEdit_contrasenia.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.lnEdit_contrasenia.setMaxLength(20)
        self.lnEdit_contrasenia.setEchoMode(QLineEdit.Password)
        self.btn_login = QPushButton(mainWindow)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(190, 230, 93, 28))

        #========================== DATA =================================#
        self.users_dict = {}


        #========================== MAIN SLOTS ===========================#

        self.btn_login.clicked.connect(self.instantiate_dashboard)





        #========================== LAST CONFIGS ===========================#

        self.retranslateUi(mainWindow)
        QMetaObject.connectSlotsByName(mainWindow)

    def read_user_data(self):
        '''Method that reads the csv file and reorganize the information in a dict object with this meanings:
        
        1. [key] > The user account.
        2. [value] > The user password.
        
        This method is always executed as a background process when the main is executed.
        '''
        with open('usuarios.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                self.users_dict[row[0]] = row[1]

    def instantiate_dashboard(self):
        '''Instantiates the dashboard window BUT only if the user exists in the csv file.
        
        That means that an username/password pair must strictly exist in the csv file.
        '''
        if not self.lnEdit_usuario.text():
            print("You haven't write any username.")
            return
        if not self.lnEdit_contrasenia.text():
            print("You haven't write any password.")
            return

        if not self.lnEdit_usuario.text() in self.users_dict:
            print("That user does not exists.")
            return

        if self.lnEdit_contrasenia.text() == self.users_dict[self.lnEdit_usuario.text()]:
            self.window2.show()
            self.mainWindow.hide()
            self.ui2.load_current_user((self.lnEdit_usuario.text(), self.lnEdit_contrasenia.text()))


    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.lnEdit_usuario.setText("")
        self.lbl_usuario.setText(QCoreApplication.translate("Form", u"Usuario", None))
        self.lbl_contrasenia.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.lnEdit_contrasenia.setText("")
        self.btn_login.setText(QCoreApplication.translate("Form", u"Iniciar sesi\u00f3n", None))
    # retranslateUi

