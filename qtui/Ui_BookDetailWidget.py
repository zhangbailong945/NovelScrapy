# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\NovelScrapy\qtui\BookDetailWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookDetailWidget(object):
    def setupUi(self, BookDetailWidget):
        BookDetailWidget.setObjectName("BookDetailWidget")
        BookDetailWidget.resize(610, 610)
        BookDetailWidget.setMinimumSize(QtCore.QSize(610, 610))
        BookDetailWidget.setMaximumSize(QtCore.QSize(610, 610))
        self.contentTextEdit = QtWidgets.QTextEdit(BookDetailWidget)
        self.contentTextEdit.setGeometry(QtCore.QRect(60, 50, 491, 471))
        self.contentTextEdit.setObjectName("contentTextEdit")
        self.widget = QtWidgets.QWidget(BookDetailWidget)
        self.widget.setGeometry(QtCore.QRect(60, 20, 491, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chapterLabel = QtWidgets.QLabel(self.widget)
        self.chapterLabel.setObjectName("chapterLabel")
        self.horizontalLayout.addWidget(self.chapterLabel)
        self.nameLabel = QtWidgets.QLabel(self.widget)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout.addWidget(self.nameLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.titleLabel = QtWidgets.QLabel(self.widget)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout.addWidget(self.titleLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.widget1 = QtWidgets.QWidget(BookDetailWidget)
        self.widget1.setGeometry(QtCore.QRect(60, 540, 491, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.previousBtn = QtWidgets.QPushButton(self.widget1)
        self.previousBtn.setObjectName("previousBtn")
        self.horizontalLayout_3.addWidget(self.previousBtn)
        self.chapterHSlider = QtWidgets.QSlider(self.widget1)
        self.chapterHSlider.setOrientation(QtCore.Qt.Horizontal)
        self.chapterHSlider.setObjectName("chapterHSlider")
        self.horizontalLayout_3.addWidget(self.chapterHSlider)
        self.nextBtn = QtWidgets.QPushButton(self.widget1)
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout_3.addWidget(self.nextBtn)
        self.widget2 = QtWidgets.QWidget(BookDetailWidget)
        self.widget2.setGeometry(QtCore.QRect(60, 580, 491, 25))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.catalogBtn = QtWidgets.QPushButton(self.widget2)
        self.catalogBtn.setObjectName("catalogBtn")
        self.horizontalLayout_4.addWidget(self.catalogBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.cacheBtn = QtWidgets.QPushButton(self.widget2)
        self.cacheBtn.setObjectName("cacheBtn")
        self.horizontalLayout_4.addWidget(self.cacheBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.lightBtn = QtWidgets.QPushButton(self.widget2)
        self.lightBtn.setObjectName("lightBtn")
        self.horizontalLayout_4.addWidget(self.lightBtn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.settingBtn = QtWidgets.QPushButton(self.widget2)
        self.settingBtn.setObjectName("settingBtn")
        self.horizontalLayout_4.addWidget(self.settingBtn)

        self.retranslateUi(BookDetailWidget)
        QtCore.QMetaObject.connectSlotsByName(BookDetailWidget)

    def retranslateUi(self, BookDetailWidget):
        _translate = QtCore.QCoreApplication.translate
        BookDetailWidget.setWindowTitle(_translate("BookDetailWidget", "Form"))
        self.contentTextEdit.setHtml(_translate("BookDetailWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> 西土。</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    一座巨大的城池从秦牧面前狂奔而过，秦牧怔然，急忙高声道：“来者是禾依依姐姐么？”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    那座奔跑的城市放慢脚步，城头上立着几尊神祇，探出头来，道：“这是白帝城的座驾，不是什么姐姐。你是何人？”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    秦牧道：“牧天尊。敢问上苍学宫是否归入白帝门下？”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    城头上一尊神祇道：“上苍学宫？你是说上苍？那并非是我白帝城的势力，那里有个叫齐九嶷的，是赤帝齐暇瑜的徒弟。赤帝便与白帝商议，把西土分了一半，赤帝又把南土分了一半给白帝……你刚才说你是谁？”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    “牧天尊。”秦牧笑道。</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    那城楼上几尊神祇回过神来，面面相觑。</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    秦牧问道：“那么，上苍学宫怎么走？”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    那几尊神祇商议片刻，一尊神祇道：“天尊请看。那边淡青色的诸天，便是上苍。天尊来到上苍下，便可以遇到那里的人，问他们便知道上苍学宫的准确方位。”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    秦牧称谢，让龙麒麟赶往上苍诸天的方向，道：“我从前觉得上苍好生神秘，监察大墟和延康的动静。现在才知道，原来上苍不过是元界的诸天万界之一，算不得什么。”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    龙麒麟道：“教主，从前你只是个小神通者，觉得上苍是个恐怖的庞然大物。现在你是牧天尊，再看上苍也不过如此了。”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    秦牧笑道：“龙胖越来越有见地了。你也是如此，也成长了。”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    那几尊神祇目送他们远去，又是面面相觑，一位神祇道：“牧天尊来到元界西土了，要不要通知白帝城？”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    “他是去赤帝的，倘若我白帝城的强者堵截他，岂不是要得罪赤帝？”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    一位年长的神祇毕竟老成，道：“况且他又是天尊，谁敢动他？由他去便是。”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    那几位神祇称是，这座大城又迈开脚步，浓烟滚滚，飞奔而去。</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    秦牧一路上遇到许多这样的陆地飞城，速度极快，都是西土的神魔用来赶路的代步工具，搬运军队，四处平叛，极为方便。</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    “这是真天宫的法术，不过真天宫正是来自域外天庭。”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    秦牧低声道：“真天老母便是域外天庭的一尊真神，多半真天老母便是白帝的麾下……”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    西土因为有上苍和真天宫的缘故，经历的战火并没有延康那般恐怖，这里的百姓还算可以维持生计。</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    秦牧来到赤帝的领地，发现这里治理得比白帝领地更好一些，西土百姓安居乐业，似乎与从前并无区别。</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    有些西土的女孩儿见到他，竟然还认得他，主动招呼。</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    “而今没有上苍学宫了，只有上苍神宗，宗主是原来的上苍学宫大祭酒虚生花。”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    那些女孩告诉他：“至于齐九嶷，那就更了不起了，上苍神宗的宗主他是看不上眼，而今住在赤帝行宫里，是西土的少主，管控着西土半壁江山的神魔，威风得很哩！”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    龙麒麟兴奋道：“齐九嶷是我弟弟！”</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    “虚生花果然聪明，把上苍学宫改成上苍神宗，</p></body></html>"))
        self.chapterLabel.setText(_translate("BookDetailWidget", "第906章"))
        self.nameLabel.setText(_translate("BookDetailWidget", "西土虚生花"))
        self.titleLabel.setText(_translate("BookDetailWidget", "牧神记"))
        self.previousBtn.setText(_translate("BookDetailWidget", "上一章"))
        self.nextBtn.setText(_translate("BookDetailWidget", "下一章"))
        self.catalogBtn.setText(_translate("BookDetailWidget", "目录"))
        self.cacheBtn.setText(_translate("BookDetailWidget", "缓存"))
        self.lightBtn.setText(_translate("BookDetailWidget", "夜间"))
        self.settingBtn.setText(_translate("BookDetailWidget", "设置"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BookDetailWidget = QtWidgets.QWidget()
    ui = Ui_BookDetailWidget()
    ui.setupUi(BookDetailWidget)
    BookDetailWidget.show()
    sys.exit(app.exec_())

