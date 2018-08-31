
import sys
from QtUiFiles.Ui_IndexWidget import Ui_IndexWidget
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QFontDatabase
from Utils.Tools import readData,initLog

class IndexWidget(QWidget,Ui_IndexWidget):

    def __init__(self,*args,**kwargs):
        super(IndexWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)


if __name__=='__main__':
    app=QApplication(sys.argv)
    w=IndexWidget()
    w.show()
    sys.exit(app.exec_())
