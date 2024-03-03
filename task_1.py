from PyQt5.QtWidgets import *
import sys
import logging as log

class Focus(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Focus with words")
        self.resize(270, 110)

        self.qle_1 = QLineEdit(self)
        self.qle_2 = QLineEdit(self)
        self.btn = QPushButton("->", self)
        self.btn.clicked.connect(self.click)

        hbox = QHBoxLayout()
        hbox.addWidget(self.qle_1, 0)
        hbox.addWidget(self.btn, 1)
        hbox.addWidget(self.qle_2, 2)
        self.setLayout(hbox)

    
    def click(self):
        if self.btn.text() == "->":
            self.btn.setText("<-")
        else:
            self.btn.setText("->")
        temp = self.qle_1.text()
        self.qle_1.setText(self.qle_2.text())
        self.qle_2.setText(temp)
        log.info("Words are changed")
        


if __name__ == "__main__":
    log.basicConfig(level=log.INFO)
    app = QApplication(sys.argv)
    fcs = Focus()
    fcs.show()
    app.exec()
