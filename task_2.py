from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys
import logging as log

class Focus(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Eval expression")
        self.resize(270, 110)

        self.qle_1 = QLineEdit()
        self.qle_2 = QLineEdit()
        self.btn = QPushButton("->")
        self.btn.clicked.connect(self.click)

        l2 = QLabel("Результат:")
        l2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        vbox = QVBoxLayout()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLabel("Выражение:"), 0)
        hbox1.addWidget(l2, 1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.qle_1, 0)
        hbox2.addWidget(self.btn, 1)
        hbox2.addWidget(self.qle_2, 2)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

    
    def click(self):
        try:
            self.qle_2.setText(str(eval(self.qle_1.text())))
        except:
            log.warning("Bad querry")
        else:
            log.info("Eval")
        


if __name__ == "__main__":
    log.basicConfig(level=log.INFO)
    app = QApplication(sys.argv)
    fcs = Focus()
    fcs.show()
    app.exec()
