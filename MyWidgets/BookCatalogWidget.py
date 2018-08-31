
import sys
from QtUiFiles.Ui_BookCatalogWidget import Ui_BookCatalogWidget
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtWidgets import QWidget,QApplication,QStackedLayout
from PyQt5.QtGui import QFontDatabase
from Utils.Tools import readData,initLog

class BookCatalogWidget(QWidget,Ui_BookCatalogWidget):

    def __init__(self,*args,**kwargs):
        super(BookCatalogWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=BookCatalogWidget()
    w.show()
    sys.exit(app.exec_())
