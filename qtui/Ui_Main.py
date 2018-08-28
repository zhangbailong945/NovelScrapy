# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\eric6Projects\NovelScrapy\qtui\Main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(771, 597)
        self.leftMenu = QtWidgets.QWidget(Main)
        self.leftMenu.setGeometry(QtCore.QRect(0, -1, 171, 551))
        self.leftMenu.setAutoFillBackground(False)
        self.leftMenu.setObjectName("leftMenu")
        self.indexBtn = QtWidgets.QPushButton(self.leftMenu)
        self.indexBtn.setGeometry(QtCore.QRect(0, 0, 171, 41))
        self.indexBtn.setCheckable(True)
        self.indexBtn.setChecked(True)
        self.indexBtn.setAutoRepeat(False)
        self.indexBtn.setObjectName("indexBtn")
        self.bookRackBtn = QtWidgets.QPushButton(self.leftMenu)
        self.bookRackBtn.setGeometry(QtCore.QRect(0, 40, 171, 41))
        self.bookRackBtn.setCheckable(False)
        self.bookRackBtn.setObjectName("bookRackBtn")
        self.aboutBtn = QtWidgets.QPushButton(self.leftMenu)
        self.aboutBtn.setGeometry(QtCore.QRect(0, 80, 171, 41))
        self.aboutBtn.setCheckable(False)
        self.aboutBtn.setObjectName("aboutBtn")
        self.updateBtn = QtWidgets.QPushButton(self.leftMenu)
        self.updateBtn.setGeometry(QtCore.QRect(0, 120, 171, 41))
        self.updateBtn.setCheckable(False)
        self.updateBtn.setChecked(False)
        self.updateBtn.setObjectName("updateBtn")
        self.bottomStatus = QtWidgets.QWidget(Main)
        self.bottomStatus.setGeometry(QtCore.QRect(0, 550, 771, 51))
        self.bottomStatus.setObjectName("bottomStatus")
        self.statusLabel = QtWidgets.QLabel(self.bottomStatus)
        self.statusLabel.setGeometry(QtCore.QRect(30, 20, 54, 12))
        self.statusLabel.setObjectName("statusLabel")
        self.rightContent = QtWidgets.QFrame(Main)
        self.rightContent.setGeometry(QtCore.QRect(179, -1, 591, 551))
        self.rightContent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightContent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightContent.setObjectName("rightContent")
        self.stackedContent = QtWidgets.QStackedWidget(self.rightContent)
        self.stackedContent.setGeometry(QtCore.QRect(-10, 0, 611, 551))
        self.stackedContent.setObjectName("stackedContent")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedContent.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedContent.addWidget(self.page_2)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Form"))
        self.indexBtn.setText(_translate("Main", "首页"))
        self.bookRackBtn.setText(_translate("Main", "我的书架"))
        self.aboutBtn.setText(_translate("Main", "关于"))
        self.updateBtn.setText(_translate("Main", "更新"))
        self.statusLabel.setText(_translate("Main", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

