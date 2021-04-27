##
# @package interpreter
#

from .basics.number_class import Number
from .basics.nodes import *

##
# @brief Interpreter class for executing functions based on input node tree
#
class Interpreter:
  def interpret(self, node:Node) -> Number:
    pass