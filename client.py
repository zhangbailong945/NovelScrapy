import sys

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

from Utils.Tools import readData
from MyWidgets.Main import Main

def main():
    app=QApplication(sys.argv)
    app.setStyleSheet(readData('Resources/Themes/Default.qss'))
    QFontDatabase.addApplicationFont('Resources/Font/Default.ttf')
    w=Main()
    w.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()