import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *
import qdarkstyle
from SignIn import SignInWidget
from SignUp import SignUpWidget
import sip
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
from mainpage_kk import Single
from changePasswordDialog import changePasswordDialog
#from Multi import  Multi

class StudentHome(QWidget):
    def __init__(self,studentId):
        super().__init__()
        self.StudentId = studentId
        self.setUpUI()

    def setUpUI(self):
        self.single_txt()
        #self.setWindowTitle("请选择类型")
        #self.layout = QHBoxLayout(self)
        #self.mutBtn = QPushButton("开启")
        #self.layout.addWidget(self.singleBtn)
        #self.layout.addWidget(self.mutBtn)
        # 绑定要执行的事件
        #self.singleBtn.clicked.connect(self.single_txt)
        #self.mutBtn.clicked.connect(self.multi_txt)
        #self.setLayout(self.layout)

    def single_txt(self):
        # sip.delete(self.widget)
        addDialog = Single(self)
        # addDialog.add_book_success_signal.connect(self.storageView.searchButtonClicked)
        addDialog.show()
        addDialog.exec_()

    def multi_txt(self):
        addDialog = Multi(self)
        # addDialog.add_book_success_signal.connect(self.storageView.searchButtonClicked)
        addDialog.show()
        addDialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = StudentHome("PB15000135")
    mainMindow.show()
    sys.exit(app.exec_())
