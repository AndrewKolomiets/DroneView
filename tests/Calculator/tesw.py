from PySide2.QtWidgets import QApplication, QMainWindow
from GUI_UI.ui_Main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        print("🟡 Начало __init__ MainWindow")
        super().__init__()
        print("🟡 После super().__init__()")

        # Проверяем, что класс правильно инициализируется
        print(f"Тип класса Ui_MainWindow: {type(self)}")

        # Проверяем, есть ли метод setupUi у экземпляра
        if hasattr(self, 'setupUi'):
            print("Метод setupUi существует!")
            try:
                self.setupUi(self)
                print("🟡 После setupUi()")
            except Exception as e:
                print(f"Ошибка при вызове setupUi: {e}")
        else:
            print("Метод setupUi не существует!")

if __name__ == "__main__":
    app = QApplication([])
    print("app start")
    window = MainWindow()
    print("window created")
    window.show()
    app.exec_()



