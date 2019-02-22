import sys
import qdarkstyle

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

from Utils.Tools import readData
from MyWidgets.Main import Main

def main():
    app=QApplication(sys.argv)
    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    app.setStyleSheet(readData('Resources/Themes/Default.qss'))
    app.setStyleSheet(dark_stylesheet)
    w=Main()
    w.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()