##
# @package library_tests
#

import unittest
from mathLib import MathFunctions

##
# @brief Test mathematic operations of math library
#
class MathLibTestBasicFunctions(unittest.TestCase):
  pass

if __name__ == '__main__':
  try:
    unittest.main()
  except Exception as e:
    print(f"Compiling of test failed\n{e}")