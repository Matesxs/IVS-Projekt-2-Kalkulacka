##
# @package math_functions
#

import math

##
# @brief Holds all mathematic functions of library
#
class MathFunctions:
  
  ##
  # @brief Addition
  #
  @staticmethod
  def add_operation(num1, num2):
    return num1 + num2

  ##
  # @brief Subtraction
  #
  @staticmethod
  def sub_operation(num1, num2):
    return num1 - num2

  ##
  # @brief Multiplication
  #
  @staticmethod
  def multiply_operation(num1, num2):
    return num1 * num2

  ##
  # @brief Division
  #
  @staticmethod
  def divide_operation(num1, num2):
    if num2 == 0:
      raise ZeroDivisionError("Can not divide by zero")
    return num1 / num2

  ##
  # @brief Power
  #
  @staticmethod
  def power_operation(num1, num2):
    if num1 < 0 and int(num2) != num2:
      raise RuntimeError("Negative number can not be raised to the power of floating point number")
    else:
      return num1 ** num2

  ##
  # @brief Root
  #
  @staticmethod
  def root_operation(n, value):
    if n == 0:
      raise RuntimeError("0th root is not defined")
    elif value < 0:
      raise RuntimeError("Can not do root of negative number")
    else:
      return value ** (1 / n)

  ##
  # @brief Invertion
  #
  @staticmethod
  def invert_operation(num):
    return -num

  ##
  # @brief Factorial
  #
  @staticmethod
  def factorial_operation(num):
    factorial = 1
    if num != int(num):
      raise RuntimeError("Factorial is not defined for floating point numbers")
    elif num < 0:
      raise RuntimeError("Factorial is not defined for negative numbers")
    elif num == 0:
      return 1
    #else:
    #  return num * factorial_operation(num - 1)
    else:
      for i in range(num):
        factorial *= (i + 1)
      return factorial

  ##
  # @brief Natural logarithm
  #
  @staticmethod
  def natural_log_operation(num):
    if num <= 0:
      raise RuntimeError("Logarithm is defined for positive numbers only")
    else:
      return math.log(num)

  ##
  # @brief Absolute value
  #
  @staticmethod
  def abs_operation(num):
    if num < 0:
      return -num
    else:
      return num