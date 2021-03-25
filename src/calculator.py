##
# @package calculator
#

from app_ui import Ui_Calculator
from PyQt5 import QtWidgets

##
# @brief Class for connection between GUI and math library
#
class CalculatorApp(QtWidgets.QMainWindow, Ui_Calculator):
  ##
  # @brief Initialization calculator
  #
  # Connection between UI and math library
  #
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.show()