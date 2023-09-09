#!/usr/bin/python3
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import qdarkstyle
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        style = qdarkstyle.load_stylesheet_pyqt5()
        self.setStyleSheet(style)
        loadUi("form.ui",self)
        self.setWindowTitle("Tic Tac Toe")
        self.setWindowIcon(QIcon("icon.png"))
        self.counter = 0
        self.pushButton_1.clicked.connect(lambda: self.clicker(self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda: self.clicker(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.clicker(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.clicker(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.clicker(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.clicker(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.clicker(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.clicker(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: self.clicker(self.pushButton_9))
        self.reset_btn.clicked.connect(self.reset_game)
    def checkWin(self):
        if self.pushButton_1.text() != "" and self.pushButton_1.text() == self.pushButton_4.text() and self.pushButton_1.text() == self.pushButton_7.text():
            self.win(self.pushButton_1,self.pushButton_4,self.pushButton_7)
        if self.pushButton_2.text() != "" and self.pushButton_2.text() == self.pushButton_5.text() and self.pushButton_2.text() == self.pushButton_8.text():
            self.win(self.pushButton_2,self.pushButton_5,self.pushButton_8)
        if self.pushButton_3.text() != "" and self.pushButton_3.text() == self.pushButton_6.text() and self.pushButton_3.text() == self.pushButton_9.text():
            self.win(self.pushButton_3,self.pushButton_6,self.pushButton_9)
        
        if self.pushButton_1.text() != "" and self.pushButton_1.text() == self.pushButton_2.text() and self.pushButton_1.text() == self.pushButton_3.text():
            self.win(self.pushButton_1,self.pushButton_2,self.pushButton_3)
        if self.pushButton_4.text() != "" and self.pushButton_4.text() == self.pushButton_6.text() and self.pushButton_4.text() == self.pushButton_6.text():
            self.win(self.pushButton_4,self.pushButton_5,self.pushButton_6)
        if self.pushButton_7.text() != "" and self.pushButton_7.text() == self.pushButton_8.text() and self.pushButton_7.text() == self.pushButton_9.text():
            self.win(self.pushButton_7,self.pushButton_8,self.pushButton_9)
        
        if self.pushButton_1.text() != "" and self.pushButton_1.text() == self.pushButton_5.text() and self.pushButton_1.text() == self.pushButton_9.text():
            self.win(self.pushButton_1,self.pushButton_5,self.pushButton_9)
        if self.pushButton_3.text() != "" and self.pushButton_3.text() == self.pushButton_5.text() and self.pushButton_3.text() == self.pushButton_7.text():
            self.win(self.pushButton_3,self.pushButton_5,self.pushButton_7)
    def win(self,a,b,c):
        a.setStyleSheet("QPushButton {color: red}")
        b.setStyleSheet("QPushButton {color: red}")
        c.setStyleSheet("QPushButton {color: red}")
        self.label.setText(f"{a.text()} Is Win!")
        self.disable()
        
    def disable(self):
        button_list = [
            self.pushButton_1,
            self.pushButton_2,
            self.pushButton_3,
            self.pushButton_4,
            self.pushButton_5,
            self.pushButton_6,
            self.pushButton_7,
            self.pushButton_8,
            self.pushButton_9,]
        for btn in button_list:
            btn.setEnabled(False)
    def clicker(self,button):
        if self.counter % 2 == 0:
            mark = "X"
            self.label.setText("O's Turn")
        else:
            mark = "O"
            self.label.setText("X's Turn")
        button.setText(mark) 
        button.setEnabled(False)
        self.counter += 1
        self.checkWin()
    def reset_game(self):
        button_list = [
            self.pushButton_1,
            self.pushButton_2,
            self.pushButton_3,
            self.pushButton_4,
            self.pushButton_5,
            self.pushButton_6,
            self.pushButton_7,
            self.pushButton_8,
            self.pushButton_9,]
        for btn in button_list:
            btn.setText("")
            btn.setEnabled(True)
            btn.setStyleSheet("QPushButton {color: #fff;}")
        self.label.setText("X's Goes First!")
        
        self.counter = 0
def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    