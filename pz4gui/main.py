import sys
import math
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget
from ui import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    def log(self, s: str):
        time = datetime.now().strftime("%H:%M:%S")
        self.ui.logPTE.appendPlainText(time + '        ' + s)

    def check(self):
        try:
            num1 = int(self.ui.FirstNumberLED.text())
            num2 = int(self.ui.ScndNumberLED.text())
            gcd = math.gcd(num1, num2)
            if gcd == 1 or gcd == -1:
                self.log('Числа ' + str(num1) + ' и ' + str(num2) + ' являются взаимно простыми')
            else:
                self.log('Числа ' + str(num1) + ' и ' + str(num2) + ' не являются взаимно простыми')
        except ValueError:
            self.log('Ошибка, некорректный ввод')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())