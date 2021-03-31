##
# @package library_tests
#

import unittest
import math
from mathLib import MathFunctions


##
# @brief Test mathematic operations of math library
#
class MathLibTestBasicFunctions(unittest.TestCase):
  def test_add(self):  # add function tests
    self.assertEqual(MathFunctions.add_operation(0, 1), 1)
    self.assertEqual(MathFunctions.add_operation(0, 0), 0)
    self.assertEqual(MathFunctions.add_operation(1, 0), 1)
    self.assertEqual(MathFunctions.add_operation(0, -1), -1)
    self.assertEqual(MathFunctions.add_operation(-1, 0), -1)
    self.assertEqual(MathFunctions.add_operation(1.5, 2.3), 3.8)
    self.assertEqual(MathFunctions.add_operation(100000, 900000), 1000000)

  def test_sub(self):  # subtraction function tests
    self.assertEqual(MathFunctions.sub_operation(1, 1), 0)
    self.assertEqual(MathFunctions.sub_operation(0, 1), -1)
    self.assertEqual(MathFunctions.sub_operation(1, 0), 1)
    self.assertEqual(MathFunctions.sub_operation(5.5, 4.3), 1.2)
    self.assertEqual(MathFunctions.sub_operation(-1, 1), -2)
    self.assertEqual(MathFunctions.sub_operation(5, -6), 11)
    self.assertEqual(MathFunctions.sub_operation(-5.3, -4.1), -1.2)
    self.assertEqual(MathFunctions.sub_operation(100, 5000000), -4999900)

  def test_mul(self):  # multiplication function tests
    self.assertEqual(MathFunctions.multiply_operation(1, 1), 1)
    self.assertEqual(MathFunctions.multiply_operation(1, 0), 0)
    self.assertEqual(MathFunctions.multiply_operation(0, 1), 0)
    self.assertEqual(MathFunctions.multiply_operation(5.3, 5), 26.5)
    self.assertEqual(MathFunctions.multiply_operation(1.2, 2.3), 2.76)
    self.assertEqual(MathFunctions.multiply_operation(12.345, 6.789), 83.810205)
    self.assertEqual(MathFunctions.multiply_operation(-5, 3), -15)
    self.assertEqual(MathFunctions.multiply_operation(-70, -33), 2310)
    self.assertEqual(MathFunctions.multiply_operation(-1450.1444, 789444784.8875), -1144808933913.812755)

  def test_div(self):  # division function tests
    self.assertEqual(MathFunctions.divide_operation(1, 1), 1)
    self.assertEqual(MathFunctions.divide_operation(0, 1), 0)
    self.assertEqual(MathFunctions.divide_operation(5, 5), 1)
    self.assertEqual(MathFunctions.divide_operation(10, 2), 5)
    self.assertEqual(MathFunctions.divide_operation(333, 111), 3)
    self.assertEqual(MathFunctions.divide_operation(15, 2), 7.5)
    self.assertEqual(MathFunctions.divide_operation(25, 4), 6.25)
    self.assertAlmostEqual(MathFunctions.divide_operation(159, 753), 0.21115537848, 10)
    self.assertAlmostEqual(MathFunctions.divide_operation(753, -159), -4.73584905660, 10)

  def test_div_by_zero(self):  # testing if division by 0 raises error
    with self.assertRaises(ZeroDivisionError):
      MathFunctions.divide_operation(0, 0)
    with self.assertRaises(ZeroDivisionError):
      MathFunctions.divide_operation(5, 0)
    with self.assertRaises(ZeroDivisionError):
      MathFunctions.divide_operation(-5, 0)
    with self.assertRaises(ZeroDivisionError):
      MathFunctions.divide_operation(-485.33, 0)

  def test_pow(self):  # power function tests
    self.assertEqual(MathFunctions.power_operation(1, 1), 1)
    self.assertEqual(MathFunctions.power_operation(0, 10), 0)
    self.assertEqual(MathFunctions.power_operation(10, 0), 1)
    self.assertEqual(MathFunctions.power_operation(0, 0), 1)
    self.assertEqual(MathFunctions.power_operation(2, 2), 4)
    self.assertEqual(MathFunctions.power_operation(2, 10), 1024)
    self.assertEqual(MathFunctions.power_operation(5, 3), 125)
    self.assertEqual(MathFunctions.power_operation(50, -2), 0.0004)
    self.assertEqual(MathFunctions.power_operation(50, 10), 97656250000000000)
    self.assertEqual(MathFunctions.power_operation(-5, 8), 390625)
    self.assertAlmostEqual(MathFunctions.power_operation(-80, -8), 0.000000000000000596046, 20)

  def test_root(self):  # root function tests
    self.assertEqual(MathFunctions.root_operation(1, 1), 1)
    self.assertEqual(MathFunctions.root_operation(1, 5), 5)
    self.assertAlmostEqual(MathFunctions.root_operation(10, 5), 1.17461894308, 10)
    self.assertAlmostEqual(MathFunctions.root_operation(-5, 10), 0.63095734448, 10)
    self.assertAlmostEqual(MathFunctions.root_operation(16, 2), 1.04427378242, 10)
    self.assertAlmostEqual(MathFunctions.root_operation(12.5, 3), 1.09186689961, 10)
    self.assertAlmostEqual(MathFunctions.root_operation(1.2, 3.4), 2.77267583598, 10)
    self.assertAlmostEqual(MathFunctions.root_operation(-5.6, 7.8), 0.69294280921, 10)

  def test_root_of_neg_number(self):  # testing if root of negative numbers raises error
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(2, -5)
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(2, -5.5)
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(-4, -10)
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(-8.3, -5.778)

  def test_zeroth_root(self):  # testing if 0th root raises error
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(0, 1)
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(0, 5)
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(0, 55.5)

  def test_log(self):  # natural logarithm function tests
    self.assertEqual(MathFunctions.natural_log_operation(1), 0)
    self.assertAlmostEqual(MathFunctions.natural_log_operation(2), 0.69314718056, 10)
    self.assertAlmostEqual(MathFunctions.natural_log_operation(3.4), 1.22377543162, 10)
    self.assertAlmostEqual(MathFunctions.natural_log_operation(100), 4.60517018599, 10)
    self.assertAlmostEqual(MathFunctions.natural_log_operation(100100100100), 25.3294365233, 10)

  def test_zero_log(self):  # testing if natural logarithm of 0 raises error
    with self.assertRaises(RuntimeError):
      MathFunctions.natural_log_operation(0)

  def test_neg_log(self):  # testing if natural logarithm of negative numbers raises error
    with self.assertRaises(RuntimeError):
      MathFunctions.natural_log_operation(-1)
    with self.assertRaises(RuntimeError):
      MathFunctions.natural_log_operation(-13)
    with self.assertRaises(RuntimeError):
      MathFunctions.natural_log_operation(-45.44)

  def test_fac(self):  # factorial function tests
    self.assertEqual(MathFunctions.factorial_operation(0), 1)
    self.assertEqual(MathFunctions.factorial_operation(1), 1)
    self.assertEqual(MathFunctions.factorial_operation(5), 120)
    self.assertEqual(MathFunctions.factorial_operation(10), 3628800)

  def test_non_intiger_fac(self):  # testing if factorial of non intiger numbers (float, double) raises error
    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(1.1)
    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(5.7)
    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(435.854)

  def test_neg_number_fac(self):  # testing if factorial of negative numbers raises error
    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(-1)
    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(-5)
    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(-8.3)

  def test_inv(self):  # inversion function tests
    self.assertEqual(MathFunctions.invert_operation(0), 0)
    self.assertEqual(MathFunctions.invert_operation(1), -1)
    self.assertEqual(MathFunctions.invert_operation(-1), 1)
    self.assertEqual(MathFunctions.invert_operation(50), -50)
    self.assertEqual(MathFunctions.invert_operation(-100.25), 100.25)

  def test_abs(self): # absolute value function tests
    self.assertEqual(MathFunctions.abs_operation(0), 0)
    self.assertEqual(MathFunctions.abs_operation(1), 1)
    self.assertEqual(MathFunctions.abs_operation(1.5), 1.5)
    self.assertEqual(MathFunctions.abs_operation(-1), 1)
    self.assertEqual(MathFunctions.abs_operation(-1.5), 1.5)
    self.assertEqual(MathFunctions.abs_operation(-50.485), 50.485)

##
# @brief Testing Tokenizer class of math library
#
class MathLibTestTokenizer(unittest.TestCase):
  pass

##
# @brief Testing Parser class of math library
#
class MathLibTestParser(unittest.TestCase):
  pass

##
# @brief Testing Interpreter class of math library
#
class MathLibTestInterpreter(unittest.TestCase):
  pass

##
# @brief Testing entrypoint for UI
#
class MathLibTestExpressions(unittest.TestCase):
  pass

if __name__ == '__main__':
  try:
    unittest.main()
  except Exception as e:
    print(f"Compiling of test failed\n{e}")
