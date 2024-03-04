from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLCDNumber,
    QLabel,
    QMessageBox
)

import logging
import sys


class Calc(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Calc")
        self.resize(270, 110)

        msg = QMessageBox()
        msg.setWindowTitle("ERROR!!!!!!!")
        msg.setText("U ARE DIV BY ZERO")
        msg.setIcon(QMessageBox.Critical)
        self.x = msg.exec_

        hbox = QHBoxLayout()

        vbox_1 = QVBoxLayout()
        vbox_2 = QVBoxLayout()
        vbox_3 = QVBoxLayout()
        vbox_4 = QVBoxLayout()

        self.a = QLineEdit()
        self.b = QLineEdit()
        n1 = QLabel("Первое целое число")
        n2 = QLabel("Второе целое число")
        vbox_1.addWidget(n1)
        vbox_1.addWidget(self.a, 0)
        vbox_1.addWidget(n2)
        vbox_1.addWidget(self.b, 1)

        suml = QLabel("Сумма")
        subl = QLabel("Разность")
        prol = QLabel("Произведение")
        divl = QLabel("Деление")

        vbox_4.addWidget(suml)
        vbox_4.addWidget(subl)
        vbox_4.addWidget(prol)
        vbox_4.addWidget(divl)

        self.sum = QLCDNumber()
        self.sub = QLCDNumber()
        self.pro = QLCDNumber()
        self.div = QLCDNumber()

        vbox_3.addWidget(self.sum)
        vbox_3.addWidget(self.sub)
        vbox_3.addWidget(self.pro)
        vbox_3.addWidget(self.div)

        self.btn = QPushButton("->")
        vbox_2.addWidget(self.btn)
        self.btn.clicked.connect(self.calc)

        hbox.addLayout(vbox_1)
        hbox.addLayout(vbox_2)
        hbox.addLayout(vbox_4)
        hbox.addLayout(vbox_3)

        self.setLayout(hbox)

    def calc(self) -> None:
        if not int(self.b.text()):
            self.x()
            return
        self.sum.display(str(int(self.a.text()) + int(self.b.text())))
        self.sub.display(str(int(self.a.text()) - int(self.b.text())))
        self.pro.display(str(int(self.a.text()) * int(self.b.text())))
        self.div.display(str(int(self.a.text()) / int(self.b.text())))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = QApplication(sys.argv)
    calc = Calc()
    calc.show()
    app.exec()

