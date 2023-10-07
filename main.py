from PyQt5.QtWidgets import QApplication

app = QApplication([])

from m2 import *
from m3 import *

def menu_generatoin():
    menu_win.show()
    window.hide()
btn_menu.clicked.connect(menu_generatoin)

def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu)


window.show()
app.exec_()


