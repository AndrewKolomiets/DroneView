# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.15
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
#print("Загрузка ui_Main.py")

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):  
        print("fuck!!!!!!!!!!!!!!!!!")
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        print(MainWindow) 
        MainWindow.resize(561, 315)
        print("fuck2") 
        
        font = QFont()
        print("fuck3")
        font.setPointSize(14)
        print("fuck4")
        MainWindow.setFont(font)
        print("fuck5")
        self.centralwidget = QWidget(MainWindow)
        print("fuck6")
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 321, 61))
        font1 = QFont()
        print("fuck2")        
        font1.setPointSize(30)
        self.lineEdit.setFont(font1)
        self.lineEdit.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pbtn_1 = QPushButton(self.centralwidget)
        self.pbtn_1.setObjectName(u"pbtn_1")
        self.pbtn_1.setGeometry(QRect(70, 180, 51, 51))
        self.pbtn_2 = QPushButton(self.centralwidget)
        self.pbtn_2.setObjectName(u"pbtn_2")
        self.pbtn_2.setGeometry(QRect(120, 180, 51, 51))
        self.pbtn_3 = QPushButton(self.centralwidget)
        self.pbtn_3.setObjectName(u"pbtn_3")
        self.pbtn_3.setGeometry(QRect(170, 180, 51, 51))
        self.pbtn_4 = QPushButton(self.centralwidget)
        self.pbtn_4.setObjectName(u"pbtn_4")
        self.pbtn_4.setGeometry(QRect(70, 130, 51, 51))
        self.pbtn_5 = QPushButton(self.centralwidget)
        self.pbtn_5.setObjectName(u"pbtn_5")
        self.pbtn_5.setGeometry(QRect(120, 130, 51, 51))
        self.pbtn_6 = QPushButton(self.centralwidget)
        self.pbtn_6.setObjectName(u"pbtn_6")
        self.pbtn_6.setGeometry(QRect(170, 130, 51, 51))
        self.pbtn_7 = QPushButton(self.centralwidget)
        self.pbtn_7.setObjectName(u"pbtn_7")
        self.pbtn_7.setGeometry(QRect(70, 80, 51, 51))
        self.pbtn_8 = QPushButton(self.centralwidget)
        self.pbtn_8.setObjectName(u"pbtn_8")
        self.pbtn_8.setGeometry(QRect(120, 80, 51, 51))
        self.pbtn_9 = QPushButton(self.centralwidget)
        self.pbtn_9.setObjectName(u"pbtn_9")
        self.pbtn_9.setGeometry(QRect(170, 80, 51, 51))
        self.pbtn_0 = QPushButton(self.centralwidget)
        self.pbtn_0.setObjectName(u"pbtn_0")
        self.pbtn_0.setGeometry(QRect(70, 230, 101, 51))
        self.pbtn_dot = QPushButton(self.centralwidget)
        self.pbtn_dot.setObjectName(u"pbtn_dot")
        self.pbtn_dot.setGeometry(QRect(170, 230, 51, 51))
        self.pbtn_Minus = QPushButton(self.centralwidget)
        self.pbtn_Minus.setObjectName(u"pbtn_Minus")
        self.pbtn_Minus.setGeometry(QRect(230, 130, 51, 51))
        self.pbtn_Div = QPushButton(self.centralwidget)
        self.pbtn_Div.setObjectName(u"pbtn_Div")
        self.pbtn_Div.setGeometry(QRect(230, 230, 51, 51))
        self.pbtn_Add = QPushButton(self.centralwidget)
        self.pbtn_Add.setObjectName(u"pbtn_Add")
        self.pbtn_Add.setGeometry(QRect(230, 80, 51, 51))
        self.pbtn_Multiple = QPushButton(self.centralwidget)
        self.pbtn_Multiple.setObjectName(u"pbtn_Multiple")
        self.pbtn_Multiple.setGeometry(QRect(230, 180, 51, 51))
        self.pbtn_Sqrt = QPushButton(self.centralwidget)
        self.pbtn_Sqrt.setObjectName(u"pbtn_Sqrt")
        self.pbtn_Sqrt.setGeometry(QRect(280, 130, 51, 51))
        self.pbtn_Persent = QPushButton(self.centralwidget)
        self.pbtn_Persent.setObjectName(u"pbtn_Persent")
        self.pbtn_Persent.setGeometry(QRect(280, 80, 51, 51))
        self.pbtn_Equal = QPushButton(self.centralwidget)
        self.pbtn_Equal.setObjectName(u"pbtn_Equal")
        self.pbtn_Equal.setGeometry(QRect(280, 180, 51, 101))
        self.pbtn_MemOut = QPushButton(self.centralwidget)
        self.pbtn_MemOut.setObjectName(u"pbtn_MemOut")
        self.pbtn_MemOut.setGeometry(QRect(10, 130, 51, 51))
        self.pbtn_Clear = QPushButton(self.centralwidget)
        self.pbtn_Clear.setObjectName(u"pbtn_Clear")
        self.pbtn_Clear.setGeometry(QRect(10, 230, 51, 51))
        self.pbtn_MemClear = QPushButton(self.centralwidget)
        self.pbtn_MemClear.setObjectName(u"pbtn_MemClear")
        self.pbtn_MemClear.setGeometry(QRect(10, 80, 51, 51))
        self.pbtn_MemAdd = QPushButton(self.centralwidget)
        self.pbtn_MemAdd.setObjectName(u"pbtn_MemAdd")
        self.pbtn_MemAdd.setGeometry(QRect(10, 180, 51, 51))
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(340, 10, 211, 271))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 561, 23))
        font2 = QFont()
        font2.setPointSize(10)
        self.menubar.setFont(font2)
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        print("oh!!!!!!!!!!!!!!!!!!!!!!!!")
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pbtn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pbtn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pbtn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pbtn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pbtn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pbtn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pbtn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pbtn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pbtn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pbtn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pbtn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pbtn_Minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pbtn_Div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pbtn_Add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pbtn_Multiple.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pbtn_Sqrt.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.pbtn_Persent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.pbtn_Equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pbtn_MemOut.setText(QCoreApplication.translate("MainWindow", u"MO", None))
        self.pbtn_Clear.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.pbtn_MemClear.setText(QCoreApplication.translate("MainWindow", u"MC", None))
        self.pbtn_MemAdd.setText(QCoreApplication.translate("MainWindow", u"MA", None))
    # retranslateUi

