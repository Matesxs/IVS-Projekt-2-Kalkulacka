##
# @package tokens
#

from dataclasses import dataclass
from enum import Enum

##
# @brief Enum class for holding token type
#
class TokenType(Enum):
      
  ## Represents any numeric value
  NUMBER    =   0

  ## Represents symbol +
  PLUS      =   1

  ## Represents symbol -
  MINUS     =   2

  ## Represents symbol *
  MULTIPLY  =   3

  ## Represents symbol /
  DIVIDE    =   4

  ## Represents symbol ^
  POW       =   5

  ## Represents symbol √
  ROOT      =   6

  ## Represents symbol (
  LPAREN    =   7

  ## Represents symbol )
  RPAREN    =   8

  ## Represents token used by its name
  KEYWORD   =   9

##
# @brief Class for holding data of each token
#
@dataclass
class Token:
  type: TokenType
  value: any = None

  ##
  # @brief Check if token matches type and value
  #
  # @param type TokenType for comparison
  # @param value Value for comparison
  # @return Bool True if they matches else False
  #
  def matches(self, type:TokenType, value):
    return self.type == type and self.value == value

  ##
  # @brief Method for printing content of token
  #
  def __repr__(self):
    return f"(TOKEN:{self.type.name}{f' VAL {self.value}' if self.value else ''})"