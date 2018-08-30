# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\NovelScrapy\qtui\BookAboutWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookAboutWidget(object):
    def setupUi(self, BookAboutWidget):
        BookAboutWidget.setObjectName("BookAboutWidget")
        BookAboutWidget.resize(610, 610)
        BookAboutWidget.setMinimumSize(QtCore.QSize(610, 610))
        BookAboutWidget.setMaximumSize(QtCore.QSize(610, 610))
        self.titleLabel = QtWidgets.QLabel(BookAboutWidget)
        self.titleLabel.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.titleLabel.setMaximumSize(QtCore.QSize(16777215, 16777211))
        self.titleLabel.setObjectName("titleLabel")
        self.nameLabel = QtWidgets.QLabel(BookAboutWidget)
        self.nameLabel.setGeometry(QtCore.QRect(40, 70, 71, 16))
        self.nameLabel.setObjectName("nameLabel")
        self.versionLabel = QtWidgets.QLabel(BookAboutWidget)
        self.versionLabel.setGeometry(QtCore.QRect(40, 100, 54, 12))
        self.versionLabel.setObjectName("versionLabel")
        self.label4 = QtWidgets.QLabel(BookAboutWidget)
        self.label4.setGeometry(QtCore.QRect(40, 130, 511, 16))
        self.label4.setObjectName("label4")
        self.siteLabel = QtWidgets.QLabel(BookAboutWidget)
        self.siteLabel.setGeometry(QtCore.QRect(40, 160, 131, 16))
        self.siteLabel.setObjectName("siteLabel")
        self.qqLabel = QtWidgets.QLabel(BookAboutWidget)
        self.qqLabel.setGeometry(QtCore.QRect(40, 190, 121, 16))
        self.qqLabel.setObjectName("qqLabel")
        self.weiboLabel = QtWidgets.QLabel(BookAboutWidget)
        self.weiboLabel.setGeometry(QtCore.QRect(40, 220, 121, 16))
        self.weiboLabel.setObjectName("weiboLabel")
        self.label8 = QtWidgets.QLabel(BookAboutWidget)
        self.label8.setGeometry(QtCore.QRect(40, 260, 511, 16))
        self.label8.setObjectName("label8")
        self.label9 = QtWidgets.QLabel(BookAboutWidget)
        self.label9.setGeometry(QtCore.QRect(40, 290, 54, 12))
        self.label9.setObjectName("label9")
        self.textEditCopyright = QtWidgets.QTextEdit(BookAboutWidget)
        self.textEditCopyright.setGeometry(QtCore.QRect(90, 310, 461, 211))
        self.textEditCopyright.setObjectName("textEditCopyright")
        self.okBtn = QtWidgets.QPushButton(BookAboutWidget)
        self.okBtn.setGeometry(QtCore.QRect(480, 540, 75, 23))
        self.okBtn.setObjectName("okBtn")

        self.retranslateUi(BookAboutWidget)
        QtCore.QMetaObject.connectSlotsByName(BookAboutWidget)

    def retranslateUi(self, BookAboutWidget):
        _translate = QtCore.QCoreApplication.translate
        BookAboutWidget.setWindowTitle(_translate("BookAboutWidget", "Form"))
        self.titleLabel.setText(_translate("BookAboutWidget", "ScrapyNovel"))
        self.nameLabel.setText(_translate("BookAboutWidget", "爬小说神器"))
        self.versionLabel.setText(_translate("BookAboutWidget", "1.0"))
        self.label4.setText(_translate("BookAboutWidget", "————————————————————————————————————————————————————————————————————————"))
        self.siteLabel.setText(_translate("BookAboutWidget", "http://www.baidu.com"))
        self.qqLabel.setText(_translate("BookAboutWidget", "QQ群：123456789"))
        self.weiboLabel.setText(_translate("BookAboutWidget", "QQ群：123456789"))
        self.label8.setText(_translate("BookAboutWidget", "————————————————————————————————————————————————————————————————————————"))
        self.label9.setText(_translate("BookAboutWidget", "特别说明："))
        self.textEditCopyright.setHtml(_translate("BookAboutWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   关于本软件，所有的书籍消息都采集于网络，如果有什么内容侵犯了你的权益，请及时与我联系。本软件仅供学习交流，切勿用于商业用途。</p></body></html>"))
        self.okBtn.setText(_translate("BookAboutWidget", "确定"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BookAboutWidget = QtWidgets.QWidget()
    ui = Ui_BookAboutWidget()
    ui.setupUi(BookAboutWidget)
    BookAboutWidget.show()
    sys.exit(app.exec_())

