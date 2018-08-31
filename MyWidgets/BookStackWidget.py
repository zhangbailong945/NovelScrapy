
import sys
from QtUiFiles.Ui_BookStackWidget import Ui_BookStackWidget
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtWidgets import QWidget,QApplication,QStackedLayout
from PyQt5.QtGui import QFontDatabase
from Utils.Tools import readData,initLog

class BookStackWidget(QWidget,Ui_BookStackWidget):

    def __init__(self,*args,**kwargs):
        super(BookStackWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)

if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setStyleSheet(readData('../Resources/Themes/Default.qss'))
    QFontDatabase.addApplicationFont('../Resources/Fonts/Deafult.ttf')
    w=BookStackWidget()
    w.show()
    sys.exit(app.exec_())


    