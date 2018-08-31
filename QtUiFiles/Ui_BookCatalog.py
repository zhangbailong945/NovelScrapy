# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\NovelScrapy\qtui\bookCatalog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 610)
        Form.setMinimumSize(QtCore.QSize(610, 610))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(5, 10, 601, 591))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(self.layoutWidget)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.authorLabel = QtWidgets.QLabel(self.layoutWidget)
        self.authorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.authorLabel.setObjectName("authorLabel")
        self.verticalLayout.addWidget(self.authorLabel)
        self.catelogListView = QtWidgets.QListView(self.layoutWidget)
        self.catelogListView.setObjectName("catelogListView")
        self.verticalLayout.addWidget(self.catelogListView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.titleLabel.setText(_translate("Form", "牧神记"))
        self.authorLabel.setText(_translate("Form", "宅猪"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

