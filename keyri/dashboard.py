# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import json
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Dashboard(object):
    def setupUi(self, vDos, mainWindow):
        #================== context ====================#

        self.vDos = vDos
        self.mainWindow = mainWindow
        
        #===============================================#

        self.passwords = None
        self.plain_passwords = []

        # ============ actual user config ============= #
        
        self.actual_username = None
        self.actual_user_password = None

        #===============================================#
        
        if not vDos.objectName():
            vDos.setObjectName(u"vDos")
        vDos.resize(745, 581)
        self.table = QTableWidget(vDos)
        if (self.table.columnCount() < 3):
            self.table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)

        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(70, 30, 491, 481))
        self.table.setColumnCount(3)

        self.btn_agregar_cuenta = QPushButton(vDos)
        self.btn_agregar_cuenta.setObjectName(u"btn_agregar_cuenta")
        self.btn_agregar_cuenta.setGeometry(QRect(590, 30, 101, 31))
        self.btn_logout = QPushButton(vDos)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setGeometry(QRect(590, 110, 101, 31))
        self.btn_logout.clicked.connect(self.logout)
        self.retranslateUi(vDos)

        QMetaObject.connectSlotsByName(vDos)

    def logout(self):
        '''Logs out.'''
        self.vDos.close()
        self.mainWindow.lnEdit_usuario.clear()
        self.mainWindow.lnEdit_contrasenia.clear()
        self.mainWindow.show()

    def load_json_data(self):
        '''Loads all user data from the json file and prepares the dataset for the table'''
        self.plain_passwords.clear()

        with open('contrasenias.json', 'r') as file:
            data = json.load(file)
        self.passwords = data[self.actual_username]
        for item in self.passwords:
            data_tuple = ()
            for key in item:
                data_tuple = list(data_tuple)
                data_tuple.append(item.get(key))
                data_tuple = tuple(data_tuple)
            self.plain_passwords.append(data_tuple)
        # print(self.plain_passwords) #debug only
            
    def load_current_user(self, usr:str):
        '''We unpack and print the current user personal information.'''

        self.actual_username, self.actual_user_password = usr
        self.load_json_data()
        self.display_information()

    def display_information(self):
        '''Retrieves all data and set up all the passwords in descendant order.'''
        self.table.setRowCount(0)
        row = 0
        for data_row in self.plain_passwords:
            self.table.insertRow(row)

            column = 0
            for value in data_row:
                item = QTableWidgetItem(str(value))
                self.table.setItem(row, column, item)
                column += 1
        row += 1












    def retranslateUi(self, vDos):
        vDos.setWindowTitle(QCoreApplication.translate("Dashboard", u"Dashboard", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("vDos", u"Servicio", None))
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("vDos", u"Usuario / cuenta", None))
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("vDos", u"Contrase\u00f1a", None))
        self.btn_agregar_cuenta.setText(QCoreApplication.translate("vDos", u"Agregar cuenta", None))
        self.btn_logout.setText(QCoreApplication.translate("vDos", u"Cerrar sesion", None))

    # retranslateUi

