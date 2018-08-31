
import sys
from QtUiFiles.Ui_BookAboutWidget import Ui_BookAboutWidget
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtWidgets import QWidget,QApplication,QStackedLayout
from PyQt5.QtGui import QFontDatabase
from Utils.Tools import readData,initLog

class BookAboutWidget(QWidget,Ui_BookAboutWidget):

    def __init__(self,*args,**kwargs):
        super(BookAboutWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=BookAboutWidget()
    w.show()
    sys.exit(app.exec_())
