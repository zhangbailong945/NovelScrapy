
import sys
from QtUiFiles.Ui_Main import Ui_Main
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtWidgets import QWidget,QApplication,QStackedLayout,QMainWindow
from PyQt5.QtGui import QFontDatabase
from Utils.Tools import readData,initLog
from MyWidgets.IndexWidget import IndexWidget
from MyWidgets.BookStackWidget import BookStackWidget
from MyWidgets.BookAboutWidget import BookAboutWidget

class Main(QWidget,Ui_Main):

    def __init__(self,*args,**kwargs):
        super(Main,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.indexBtn.clicked.connect(self.showIndex)
        self.bookRackBtn.clicked.connect(self.showBookStack)
        self.aboutBtn.clicked.connect(self.showBookAbout)
        self.indexW=IndexWidget()
        self.bookStackW=BookStackWidget()
        self.bookAboutW=BookAboutWidget()
        self.stackedContent.addWidget(self.indexW)
        self.stackedContent.addWidget(self.bookStackW)
        self.stackedContent.addWidget(self.bookAboutW)
    
    #显示首页
    def showIndex(self):
        self.stackedContent.setCurrentIndex(0)

    
    #显示我的书架
    def showBookStack(self):
        self.stackedContent.setCurrentIndex(1)

    #显示关于我们
    def showBookAbout(self):
        self.stackedContent.setCurrentIndex(2)


if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setStyleSheet(readData('../Resources/Themes/Default.qss'))
    QFontDatabase.addApplicationFont('../Resources/Fonts/Deafult.ttf')
    w=Main()
    w.show()
    sys.exit(app.exec_())


    