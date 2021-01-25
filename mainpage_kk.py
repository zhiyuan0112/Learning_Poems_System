import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import sip
import qdarkstyle
import  linecache
import collections
from tkinter import *
from main import *
import tkinter as tk
from PIL import Image,ImageTk
#from dl_layers import str2id,id2str
import os
from PoemAppreciation import *
from translate import *
class Single(QDialog):
    def __init__(self,parent=None):
        super(Single,self).__init__(parent)
        self.resize(900, 600)
        self.setWindowTitle("欢迎使用古诗词趣学系统")
        self.setUpUI()

    def setUpUI(self):
        # 总布局
        self.layout = QHBoxLayout(self)
        self.Hlayout1 = QVBoxLayout()
        self.Hlayout2 = QVBoxLayout()
        self.Hlayout11 = QVBoxLayout()
        self.Hlayout12 = QHBoxLayout()
        self.Hlayout13 = QVBoxLayout()
        self.openButton = QPushButton("选取古诗词/输入")
        self.text1Content = QTextEdit("两个黄鹂鸣翠柳，一行白鹭上青天。窗含西岭千秋雪，门泊东吴万里船。")
        self.Hlayout11.addWidget(self.openButton)
        self.Hlayout11.addWidget(self.text1Content)
        self.mid1Button = QPushButton("古诗鉴赏")
        self.mid2Button = QPushButton("古诗翻译")
        self.Hlayout12.addWidget(self.mid1Button)
        self.Hlayout12.addWidget(self.mid2Button)
        self.text2Content = QTextEdit()
        self.Hlayout13.addWidget(self.text2Content)
        self.openButton.clicked.connect(self.showDialog1)
        self.mid1Button.clicked.connect(self.show1)
        self.mid2Button.clicked.connect(self.show2)
        self.Hlayout3 = QHBoxLayout()
        self.Hlayout4 = QHBoxLayout()
        self.click = QPushButton("写诗")
        self.sumComboBox = QComboBox()
        sumCount = ['2句', '4句','8句']
        self.Hlayout3.addWidget(self.sumComboBox)
        self.sumComboBox.addItems(sumCount)
        self.con_fast = QComboBox()
        sumCount1 = ['context', 'fast']
        self.Hlayout3.addWidget(self.con_fast)
        self.con_fast.addItems(sumCount1)
        self.Hlayout3.addWidget(self.click)
        self.text3Content = QLineEdit("")
        self.unitButton = QPushButton("开头诗")
        self.Hlayout4.addWidget(self.text3Content)
        self.Hlayout4.addWidget(self.unitButton)
        self.unitButton.clicked.connect(self.Unitclick)
        self.click.clicked.connect(self.APclick)
        self.Hlayout2.addLayout(self.Hlayout3)
        self.Hlayout2.addLayout(self.Hlayout4)
        self.leftContent = QTextEdit("")
        self.Hlayout2.addWidget(self.leftContent)
        self.Hlayout1.addLayout(self.Hlayout11)
        self.Hlayout1.addLayout(self.Hlayout12)
        self.Hlayout1.addLayout(self.Hlayout13)
        self.layout.addLayout(self.Hlayout2)
        self.layout.addLayout(self.Hlayout1)


        self.setLayout(self.layout)


    def showDialog1(self):
        directory1 = QFileDialog.getOpenFileName(self, "选择文件夹", "/")
        print(directory1[0])
        with open(directory1[0], 'r', encoding='utf-8') as test:
           txt = test.read()
           test.close()
        self.text1Content.setPlainText(txt)
    def show1(self):
        chupoem = self.text1Content.toPlainText()
        poem = PoemAppreciationAPI().appreciate(chupoem)
        self.text2Content.setPlainText(poem)

    def show2(self):
        chupoem = self.text1Content.toPlainText()
        print(chupoem)
        poem = translation(chupoem)
        self.text2Content.setPlainText(poem)


    def APclick(self):
        rows = self.sumComboBox.currentText()
        int_rows = int(rows[0])
        wt = self.con_fast.currentText()
        if wt == "context":
            poem = write_poem_context(int_rows)
        else :
            poem = write_poem_fast(int_rows)
        self.leftContent.setPlainText(poem)

    def Unitclick(self):#开头诗
        begin_words = self.text3Content.text()
        poem = write_poem_head(begin_words)
        self.leftContent.setPlainText(poem)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = Single()
    mainMindow.show()
    sys.exit(app.exec_())
