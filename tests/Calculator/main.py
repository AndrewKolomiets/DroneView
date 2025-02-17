import sys
import PySide2

from PySide2.QtWidgets import QApplication, QMainWindow
#from GUI_UI.ui_Main import Ui_MainWindow
print ("Before import Ui_MainWindow")
from ui_Main import Ui_MainWindow
print ("After import Ui_MainWindow")

#print(PySide2.__version__)

#class MainWindow(QMainWindow, Ui_MainWindow):
class MainWindow(QMainWindow):
    def __init__(self):
        print("before __init__")
        super(MainWindow,self).__init__()
        print("after __init__")

        self.wgt = Ui_MainWindow()
        
        print("before setupUi")
        self.wgt.setupUi(self)
        print("after setupUi")

        print("Инициализация MainWindow")  # Добавлено для проверки
        self.initSignals()
        self.resize(600, 400)  # Задаём размер
        self.move(100, 100)  # Перемещаем в видимую область экрана

    def initSignals(self):
        #"""Подключаем кнопки к методам"""
        self.wgt.pbtn_0.clicked.connect(lambda: self.add_digit("0"))
        self.wgt.pbtn_1.clicked.connect(lambda: self.add_digit("1"))
        self.wgt.pbtn_2.clicked.connect(lambda: self.add_digit("2"))
        self.wgt.pbtn_3.clicked.connect(lambda: self.add_digit("3"))
        self.wgt.pbtn_4.clicked.connect(lambda: self.add_digit("4"))
        self.wgt.pbtn_5.clicked.connect(lambda: self.add_digit("5"))
        self.wgt.pbtn_6.clicked.connect(lambda: self.add_digit("6"))
        self.wgt.pbtn_7.clicked.connect(lambda: self.add_digit("7"))
        self.wgt.pbtn_8.clicked.connect(lambda: self.add_digit("8"))
        self.wgt.pbtn_9.clicked.connect(lambda: self.add_digit("9"))
        self.wgt.pbtn_dot.clicked.connect(lambda: self.add_digit("."))

        self.wgt.pbtn_Add.clicked.connect(lambda: self.add_operator("+"))
        self.wgt.pbtn_Minus.clicked.connect(lambda: self.add_operator("-"))
        self.wgt.pbtn_Multiple.clicked.connect(lambda: self.add_operator("*"))
        self.wgt.pbtn_Div.clicked.connect(lambda: self.add_operator("/"))

        self.wgt.pbtn_Equal.clicked.connect(self.calculate_result)
        self.wgt.pbtn_Clear.clicked.connect(self.clear_display)
    
    def add_digit(self, digit): #add digit
        text = self.wgt.lineEdit.text()
        if text == "0":
            self.wgt.lineEdit.setText(digit)
        else:
            self.wgt.lineEdit.setText(text + digit)    
    
    def add_operator(self, operator):
        #"""Добавляем оператор (+, -, *, /)"""
        text = self.wgt.lineEdit.text()
        if text[-1] not in "+-*/":
            self.wgt.lineEdit.setText(text + operator)

    def calculate_result(self):
        #"""Вычисляем выражение"""
        try:
            result = eval(self.wgt.lineEdit.text())
            self.wgt.lineEdit.setText(str(result))
        except Exception:
            self.wgt.lineEdit.setText("Ошибка")

    def clear_display(self):
        #"""Очищаем дисплей"""
        self.wgt.lineEdit.setText("0")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("app start")
    window = MainWindow()
    print("parametr window is set")
    window.show()
    print("Parameter window is show")
    sys.exit(app.exec_())
    #app.exec_()