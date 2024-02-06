from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        self.gred_lay = QGridLayout()
        self.h_lbl_lay = QHBoxLayout()
        self.setFixedSize(150, 160)
        

        self.btn1 = QPushButton(clicked = lambda: self.check(self.btn1))
        self.btn2 = QPushButton(clicked = lambda: self.check(self.btn2))
        self.btn3 = QPushButton(clicked = lambda: self.check(self.btn3))
        self.btn4 = QPushButton(clicked = lambda: self.check(self.btn4))
        self.btn5 = QPushButton(clicked = lambda: self.check(self.btn5))
        self.btn6 = QPushButton(clicked = lambda: self.check(self.btn6))
        self.btn7 = QPushButton(clicked = lambda: self.check(self.btn7))
        self.btn8 = QPushButton(clicked = lambda: self.check(self.btn8))
        self.btn9 = QPushButton(clicked = lambda: self.check(self.btn9))
        self.lst = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]

        index = 0
        for i in range(3):
            for j in range(3):
                self.gred_lay.addWidget(self.lst[index], i, j)
                self.lst[index].setStyleSheet("font-size:20px")
                self.lst[index].setFixedSize(40, 40)
                index += 1

        self.lbl = QLabel("🟢")
        self.h_lbl_lay.addStretch()
        self.h_lbl_lay.addWidget(self.lbl)
        self.h_lbl_lay.addStretch()

        self.lampochka = False

        self.v_main_lay.addLayout(self.gred_lay)
        self.v_main_lay.addLayout(self.h_lbl_lay)

        self.setLayout(self.v_main_lay)

        self.count = 0

        
    def check(self, btn):
        if self.lampochka == False:
            btn.setText("🟢")
            self.win = "🟢"
            self.lampochka = True
            self.lbl.setText("❌")
            self.count += 1
        else:
            btn.setText("❌")
            self.win = "❌"
            self.lampochka = False
            self.lbl.setText("🟢")
            self.count += 1
        btn.setEnabled(False)
        
        if self.btn1.text() == self.btn2.text() == self.btn3.text() and self.btn1.text() != "":
            self.winner()
        elif self.btn1.text() == self.btn4.text() == self.btn7.text() and self.btn1.text() != "":
            self.winner()
        elif self.btn3.text() == self.btn6.text() == self.btn9.text() and self.btn3.text() != "":
            self.winner()
        elif self.btn7.text() == self.btn8.text() == self.btn9.text() and self.btn7.text() != "":
            self.winner()
        elif self.btn2.text() == self.btn5.text() == self.btn8.text() and self.btn2.text() != "":
            self.winner()
        elif self.btn4.text() == self.btn5.text() == self.btn6.text() and self.btn4.text() != "":
            self.winner()
        elif self.btn1.text() == self.btn5.text() == self.btn9.text() and self.btn1.text() != "":
            self.winner()
        elif self.btn3.text() == self.btn5.text() == self.btn7.text() and self.btn3.text() != "":
            self.winner()
        

        if self.count == 9:
            self.lbl.setText("Durrang")

    def winner(self):
        self.lbl.setText(f"{self.win} Winner")
        for i in self.lst:
            i.setEnabled(False)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()