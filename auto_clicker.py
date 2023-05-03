import pyautogui
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QSpinBox
from PyQt5.QtWidgets import (QPushButton, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from time import sleep
from time import time

app = QApplication([])
my_win = QWidget()

def start():
    clk = int(clks.value())
    print(clk)
    sleep(5)

    pyautogui.PAUSE = 0.0

    for i in range(clk):
        pyautogui.click()

lbl = QLabel()
lbl.setText('Auto clicker')

lb = QLabel()
lb.setText('Number of clicks(not cps):')

clks = QSpinBox()
clks.setMaximum(10000)

pb = QPushButton(text='Start (you will have 5 seconds after pressing the button)')
pb.clicked.connect(start)

xv = QVBoxLayout()
xh = QHBoxLayout()

xh.addWidget(lb)
xh.addWidget(clks)

xv.addWidget(lbl)
xv.addLayout(xh)        
xv.addWidget(pb)

my_win.setLayout(xv)

my_win.show()
app.exec_()    
