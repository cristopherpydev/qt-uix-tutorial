import sys

from PySide6.QtWidgets import QApplication, QWidget
from login import Login
class MainWindow(QWidget, Login):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        

def main():
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    window.read_user_data()
    app.exec()

if __name__ == '__main__':
    main()