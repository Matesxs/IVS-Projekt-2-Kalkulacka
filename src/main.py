##
# @package main
#
# Create app UI object and show it
#

import sys
from PyQt5.QtWidgets import QApplication
from calculator import CalculatorApp

app = QApplication(sys.argv)
win = CalculatorApp()
win.show()
sys.exit(app.exec())