
import sys
from QtUiFiles.Ui_Main import Ui_Main
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtWidgets import QWidget,QApplication,QStackedLayout
from PyQt5.QtGui import QFontDatabase
from Utils.Tools import readData,initLog
from MyWidgets import IndexWidget,BookStackWidget

class Main(QWidget,Ui_Main):

    def __init__(self,*args,**kwargs):
        super(Main,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.indexBtn.clicked.connect(self.showIndex)
        self.bookRackBtn.clicked.connect(self.showBookStack)
    
    #显示首页
    def showIndex(self):
        indexW=IndexWidget()
        self.stackedContent.addWidget()
    
    #显示我的书架
    def showBookStack(self):
        bookStack=BookStackWidget()
        self.stackedContent.addWidget(bookStack)


if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setStyleSheet(readData('../Resources/Themes/Default.qss'))
    QFontDatabase.addApplicationFont('../Resources/Fonts/Deafult.ttf')
    w=Main()
    w.show()
    sys.exit(app.exec_())


    