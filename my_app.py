#1. untuk meminta izin menggunakan codingan orang lain
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
from second_win import *

#2. membuat tamplat aplikasi layar pertama ( tampilan main menu )
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

#3. membuat tampilan aplikasi layar pertama 
    def initUI(self):
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction) #untuk membuat labelnya / widgetnya 21-24
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line) #membuat layoutnya 25-29

#4. untuk menampilkan ke layar berikutnya ( layar formulir / ke 2)
    def next_click(self):
        self.tw = TestWin()
        self.hide() 
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

#5. untuk menampilkan pertamanya
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

#6. untuk menjalankan layar pertama
app = QApplication([])
mw = MainWin()
app.exec_()

#7. belum