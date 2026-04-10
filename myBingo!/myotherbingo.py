import random

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class MyBingo(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(668, 605)
        Form.setStyleSheet(u"background-color: green;")
        self.t_edit_1 = QTextEdit(Form)
        self.t_edit_1.setObjectName(u"t_edit_1")
        self.t_edit_1.setEnabled(False)
        self.t_edit_1.setGeometry(QRect(170, 150, 81, 71))
        self.t_edit_1.setAutoFillBackground(False)
        self.t_edit_1.setStyleSheet(u"background-color: white;color:black;")
        self.t_edit_2 = QTextEdit(Form)
        self.t_edit_2.setObjectName(u"t_edit_2")
        self.t_edit_2.setEnabled(False)
        self.t_edit_2.setGeometry(QRect(290, 150, 81, 71))
        self.t_edit_2.setAutoFillBackground(False)
        self.t_edit_2.setStyleSheet(u"background-color: white;color:black;")
        self.t_edit_3 = QTextEdit(Form)
        self.t_edit_3.setObjectName(u"t_edit_3")
        self.t_edit_3.setEnabled(False)
        self.t_edit_3.setGeometry(QRect(410, 150, 81, 71))
        self.t_edit_3.setAutoFillBackground(False)
        self.t_edit_3.setStyleSheet(u"background-color: white;color:black;")
        self.t_edit_4 = QTextEdit(Form)
        self.t_edit_4.setObjectName(u"t_edit_4")
        self.t_edit_4.setEnabled(False)
        self.t_edit_4.setGeometry(QRect(410, 280, 81, 71))
        self.t_edit_4.setAutoFillBackground(False)
        self.t_edit_4.setStyleSheet(u"background-color: white;color:black;")
        self.t_edit_5 = QTextEdit(Form)
        self.t_edit_5.setObjectName(u"t_edit_5")
        self.t_edit_5.setEnabled(False)
        self.t_edit_5.setGeometry(QRect(290, 280, 81, 71))
        self.t_edit_5.setAutoFillBackground(False)
        self.t_edit_5.setStyleSheet(u"background-color: white;color:black;")
        self.t_edit_6 = QTextEdit(Form)
        self.t_edit_6.setObjectName(u"t_edit_6")
        self.t_edit_6.setEnabled(False)
        self.t_edit_6.setGeometry(QRect(170, 280, 81, 71))
        self.t_edit_6.setAutoFillBackground(False)
        self.t_edit_6.setStyleSheet(u"background-color: white;color:black;")
        self.lbl_titulo = QLabel(Form)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        self.lbl_titulo.setGeometry(QRect(260, 20, 131, 41))
        font = QFont()
        font.setPointSize(20)
        self.lbl_titulo.setFont(font)
        self.btn_generar = QPushButton(Form)
        self.btn_generar.setObjectName(u"btn_generar")
        self.btn_generar.setEnabled(False)
        self.btn_generar.setGeometry(QRect(80, 450, 93, 28))
        self.btn_generar.setAutoFillBackground(False)
        self.btn_generar.setStyleSheet(u"background-color: white;color:black;")
        self.btn_guardar = QPushButton(Form)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setEnabled(False)
        self.btn_guardar.setGeometry(QRect(490, 450, 93, 28))
        self.btn_guardar.setAutoFillBackground(False)
        self.btn_guardar.setStyleSheet(u"background-color: white;color:black;")
        self.btn_comenzar = QPushButton(Form)
        self.btn_comenzar.setObjectName(u"btn_comenzar")
        self.btn_comenzar.setGeometry(QRect(290, 500, 93, 28))
        self.btn_comenzar.setAutoFillBackground(False)
        self.btn_comenzar.setStyleSheet(u"background-color: white;color:black;")
        self.lbl_titulo.raise_()
        self.btn_guardar.raise_()
        self.btn_comenzar.raise_()
        self.t_edit_3.raise_()
        self.t_edit_2.raise_()
        self.t_edit_6.raise_()
        self.btn_generar.raise_()
        self.t_edit_5.raise_()
        self.t_edit_4.raise_()
        self.t_edit_1.raise_()
        # ============================ variables and constants =========================== #

        self.is_stopped = True
        self.bingo_card = []

        # ============================ main events =========================== #

        def start_or_pause():
            '''This slot activates/disables the other buttons.'''
            if self.is_stopped:
                self.btn_comenzar.setText("Detener")
                self.is_stopped = False
                self.btn_generar.setEnabled(True)
                return
            self.btn_comenzar.setText("Comenzar")
            self.is_stopped = True
            self.btn_generar.setEnabled(False)
            return

        def generate_numbers():
            '''This slot mainly generates a 2x3 numeric matrix of 1-50 range random numbers without any repetition.'''
            if self.bingo_card:
                self.bingo_card.clear()

            for _ in range(6):
                while True:
                    my_number = str(random.randint(1,50))
                    if my_number not in self.bingo_card:
                        self.bingo_card.append(my_number)
                        break
            self.t_edit_1.setText(self.bingo_card[0])
            self.t_edit_2.setText(self.bingo_card[1])       
            self.t_edit_3.setText(self.bingo_card[2])
            self.t_edit_4.setText(self.bingo_card[3])
            self.t_edit_5.setText(self.bingo_card[4])
            self.t_edit_6.setText(self.bingo_card[5])
            self.btn_guardar.setEnabled(True)

        def save_cardboard():
            if not self.bingo_card:
                pass
            # ================ GENERATE THE CARDBOARD LAYOUT ================= #
            with open('cardboard.txt', 'w') as f:
                cardboard = ""
                for number in self.bingo_card:
                    cardboard += f"| {number} |"
                
                f.write(cardboard)

                

            # ============================ main slots =========================== #
        
        self.btn_comenzar.clicked.connect(start_or_pause) #this button displays/sets up the environment.

        self.btn_generar.clicked.connect(generate_numbers) #this button generates the numbers.

        self.btn_guardar.clicked.connect(save_cardboard) #this button saves the cardboard.


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.t_edit_1.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.lbl_titulo.setText(QCoreApplication.translate("Form", u"MyBingo!", None))
        self.btn_generar.setText(QCoreApplication.translate("Form", u"Generar", None))
        self.btn_guardar.setText(QCoreApplication.translate("Form", u"Guardar", None))
        self.btn_comenzar.setText(QCoreApplication.translate("Form", u"Comenzar", None))
    # retranslateUi

