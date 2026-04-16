import sys

from PySide6.QtWidgets import QApplication, QWidget
from layout import Layout
class MainWindow(QWidget, Layout):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        

def main():
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()