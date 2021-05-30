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
  # @param num1 Int or float
  # @param num2 Int or float
  # @return Result of addition num1 to num2
  #
  @staticmethod
  def add_operation(num1, num2):
    return num1 + num2

  ##
  # @brief Subtraction
  #
  # @param num1 Int or float
  # @param num2 Int or float
  # @return Result of subtraction num2 from num1
  #
  @staticmethod
  def sub_operation(num1, num2):
    return num1 - num2

  ##
  # @brief Multiplication
  #
  # @param num1 Int or float
  # @param num2 Int or float
  # @return Result of multiplication num1 and num2
  #
  @staticmethod
  def multiply_operation(num1, num2):
    return num1 * num2

  ##
  # @brief Division
  #
  # @warning
  # num2 can not be zero
  #
  # @param num1 Int or float
  # @param num2 Int or flaot
  # @return Result of division num1 by num2
  #
  @staticmethod
  def divide_operation(num1, num2):
    if num2 == 0:
      raise ZeroDivisionError("Can not divide by zero")
    return num1 / num2

  ##
  # @brief Power
  #
  # @warning
  # num2 must be int if num1 is negative
  #
  # @param num1 Int or float
  # @param num2 Int or float
  # @return Result of powering num1 by num2
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
  # @warning
  # value can not be negative
  # @warning
  # n can not be zero
  #
  # @param n Int or float
  # @param value Int or float
  # @return Result of nth root of value
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
  # @param num Int or float
  # @return Negation of num
  #
  @staticmethod
  def invert_operation(num):
    return -num

  ##
  # @brief Factorial
  #
  # @warning
  # num must be natural number
  # @warning
  # num can not be over 50000
  #
  # @param num Int
  # @return Factorial of num
  #
  @staticmethod
  def factorial_operation(num):
    factorial = 1
    if num != int(num):
      raise RuntimeError("Factorial is not defined for floating point numbers")
    elif num < 0:
      raise RuntimeError("Factorial is not defined for negative numbers")
    elif num > 50000:
      raise RuntimeError("Factorial is not defined for too large numbers")
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
  # @warning
  # num must be positive
  #
  # @param num Int or float
  # @return Natural logarithm of num
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
  # @param num Int or float
  # @return Absolute value of num
  #
  @staticmethod
  def abs_operation(num):
    if num < 0:
      return -num
    else:
      return num