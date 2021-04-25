##
# @package library_tests
#

import unittest
import math
from mathLib import MathFunctions, Interpreter, Parser, Tokenizer, Token, TokenType
from mathLib.basics.nodes import *

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
  
  ##
  # @brief Test empty expression
  #
  def test_empty(self):
    self.assertEqual(Tokenizer("").tokenize(), [])
    self.assertEqual(Tokenizer("   ").tokenize(), [])
    self.assertEqual(Tokenizer("\n\n\n").tokenize(), [])
    self.assertEqual(Tokenizer("\t\t\t").tokenize(), [])
    self.assertEqual(Tokenizer(" \n\t  \n \t\n  \n\t\n  ").tokenize(), [])
  
  ##
  # @brief Test numbers
  #
  def test_numbers(self):
    self.assertEqual(Tokenizer("12345").tokenize(), [Token(TokenType.NUMBER, 12345)])
    self.assertEqual(Tokenizer("67890").tokenize(), [Token(TokenType.NUMBER, 67890)])
    self.assertEqual(Tokenizer(".").tokenize(), [Token(TokenType.NUMBER, 0.0)])
    self.assertEqual(Tokenizer("9.").tokenize(), [Token(TokenType.NUMBER, 9.0)])
    self.assertEqual(Tokenizer(".9").tokenize(), [Token(TokenType.NUMBER, 0.9)])
    self.assertEqual(Tokenizer("135.097").tokenize(), [Token(TokenType.NUMBER, 135.097)])
    self.assertEqual(Tokenizer("1 2.3 .4 5. 67.89").tokenize(), [
      Token(TokenType.NUMBER, 1),
      Token(TokenType.NUMBER, 2.3),
      Token(TokenType.NUMBER, 0.4),
      Token(TokenType.NUMBER, 5.0),
      Token(TokenType.NUMBER, 67.89)
    ])
  
  ##
  # @brief Test operators
  #
  def test_operators(self):
    self.assertEqual(Tokenizer("+").tokenize(), [Token(TokenType.PLUS)])
    self.assertEqual(Tokenizer("-").tokenize(), [Token(TokenType.MINUS)])
    self.assertEqual(Tokenizer("*").tokenize(), [Token(TokenType.MULTIPLY)])
    self.assertEqual(Tokenizer("/").tokenize(), [Token(TokenType.DIVIDE)])
    self.assertEqual(Tokenizer("^").tokenize(), [Token(TokenType.POW)])
    self.assertEqual(Tokenizer("√").tokenize(), [Token(TokenType.ROOT)])
    self.assertEqual(Tokenizer("+ */^ -").tokenize(), [
      Token(TokenType.PLUS),
      Token(TokenType.MULTIPLY),
      Token(TokenType.DIVIDE),
      Token(TokenType.POW),
      Token(TokenType.MINUS)
    ])
  
  ##
  # @brief Test brackets
  #
  def test_brackets(self):
    self.assertEqual(Tokenizer("(").tokenize(), [Token(TokenType.LPAREN)])
    self.assertEqual(Tokenizer(")").tokenize(), [Token(TokenType.RPAREN)])
    self.assertEqual(Tokenizer("()").tokenize(), [
      Token(TokenType.LPAREN),
      Token(TokenType.RPAREN)
    ])
    self.assertEqual(Tokenizer(")(())(").tokenize(), [
      Token(TokenType.RPAREN),
      Token(TokenType.LPAREN),
      Token(TokenType.LPAREN),
      Token(TokenType.RPAREN),
      Token(TokenType.RPAREN),
      Token(TokenType.LPAREN)
    ])
  
  ##
  # @brief Test keywords
  #
  def test_keywords(self):
    self.assertEqual(Tokenizer("e").tokenize(), [Token(TokenType.KEYWORD, e)])
    self.assertEqual(Tokenizer("abs").tokenize(), [Token(TokenType.KEYWORD, abs)])
    self.assertEqual(Tokenizer("ln").tokenize(), [Token(TokenType.KEYWORD, ln)])
    self.assertEqual(Tokenizer("fact").tokenize(), [Token(TokenType.KEYWORD, fact)])
    self.assertEqual(Tokenizer("rand").tokenize(), [Token(TokenType.KEYWORD, rand)])
    self.assertEqual(Tokenizer("abs fact ln").tokenize(), [
      Token(TokenType.KEYWORD, abs),
      Token(TokenType.KEYWORD, fact),
      Token(TokenType.KEYWORD, ln)
    ])
  
  ##
  # @brief Test combined expression
  #
  def test_combined_expression(self):
    self.assertEqual(Tokenizer("abs( 10.01 ^(9/ 3)- 15\n*ln(e* e)) +rand*2.5\t +3√18- 654321 \n*fact(4.)+.15").tokenize(), [
      Token(TokenType.KEYWORD, abs),
      Token(TokenType.LPAREN),
      Token(TokenType.NUMBER, 10.01),
      Token(TokenType.POW),
      Token(TokenType.LPAREN),
      Token(TokenType.NUMBER, 9),
      Token(TokenType.DIVIDE),
      Token(TokenType.NUMBER, 3),
      Token(TokenType.RPAREN),
      Token(TokenType.MINUS),
      Token(TokenType.NUMBER, 15),
      Token(TokenType.MULTIPLY),
      Token(TokenType.KEYWORD, ln),
      Token(TokenType.LPAREN),
      Token(TokenType.KEYWORD, e),
      Token(TokenType.MULTIPLY),
      Token(TokenType.KEYWORD, e),
      Token(TokenType.RPAREN),
      Token(TokenType.RPAREN),
      Token(TokenType.PLUS),
      Token(TokenType.KEYWORD, rand),
      Token(TokenType.MULTIPLY),
      Token(TokenType.NUMBER, 2.5),
      Token(TokenType.PLUS),
      Token(TokenType.NUMBER, 3),
      Token(TokenType.ROOT),
      Token(TokenType.NUMBER, 18),
      Token(TokenType.MINUS),
      Token(TokenType.NUMBER, 654321),
      Token(TokenType.MULTIPLY),
      Token(TokenType.KEYWORD, fact),
      Token(TokenType.LPAREN),
      Token(TokenType.NUMBER, 4.0),
      Token(TokenType.RPAREN),
      Token(TokenType.PLUS),
      Token(TokenType.NUMBER, 0.15),
    ])
  
  ##
  # @brief Test multiple decimal dots
  #
  def test_multidecdots(self):
    self.assertEqual(Tokenizer("...").tokenize(), [
      Token(TokenType.NUMBER, 0.0),
      Token(TokenType.NUMBER, 0.0),
      Token(TokenType.NUMBER, 0.0)
    ])
  
  ##
  # @brief Test invalid characters
  #
  def test_invalid_char(self):
    with self.assertRaises(SyntaxError):
      Tokenizer(""",:;?!|%$@#'"´ˇ""").tokenize()
    with self.assertRaises(SyntaxError):
      Tokenizer("5+8'12#3*6!").tokenize()
    with self.assertRaises(SyntaxError):
      Tokenizer("0|1%2$3@4").tokenize()
  
  ##
  # @brief Test invalid expressions
  #
  def test_invalid_expression(self):
    with self.assertRaises(SyntaxError):
      Tokenizer("abselnfactrand").tokenize()
    with self.assertRaises(SyntaxError):
      Tokenizer("sin(10)").tokenize()
    with self.assertRaises(SyntaxError):
      Tokenizer("cos(10)").tokenize()
    with self.assertRaises(SyntaxError):
      Tokenizer("tan(10)").tokenize()
    with self.assertRaises(SyntaxError):
      Tokenizer("ab(5) + factln(10) - erand").tokenize()
    with self.assertRaises(SyntaxError):
      Tokenizer("14 5 * 9 82 - abs( 7 10)").tokenize()
    with self.assertRaises(SyntaxError):
      Tokenizer("Hello world!").tokenize()

##
# @brief Testing Parser class of math library
#
class MathLibTestParser(unittest.TestCase):
  ##
  # @brief Test empty list of tokens
  #
  def test_empty(self):
    node_tree = Parser([]).parse()
    self.assertEqual(node_tree, None)

  ##
  # @brief Test unknown tokens
  #
  def test_unknown_token(self):
    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fafsafasfasfasfasfawsfwa")]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "randbla")]).parse()

  ##
  # @brief Test parsing numbers
  #
  def test_numbers(self):
    self.assertEqual(Parser([Token(TokenType.NUMBER, 124.34)]).parse(), NumberNode(124.34))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 321)]).parse(), NumberNode(321))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 0)]).parse(), NumberNode(0))
    self.assertEqual(Parser([Token(TokenType.NUMBER, -51.3)]).parse(), NumberNode(-51.3))
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "e")]).parse(), NumberNode(math.e))
    self.assertIsInstance(Parser([Token(TokenType.KEYWORD, "rand")]).parse(), NumberNode)

  ##
  # @brief Test parsing binary operations
  #
  def test_binary_operations(self):
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.PLUS), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.MINUS), Token(TokenType.NUMBER, 50)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.MINUS), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.MULTIPLY), Token(TokenType.NUMBER, 50)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.MULTIPLY), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.DIVIDE), Token(TokenType.NUMBER, 50)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.DIVIDE), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.POW), Token(TokenType.NUMBER, 50)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.POW), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.ROOT), Token(TokenType.NUMBER, 50)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.ROOT), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.DIVIDE), Token(TokenType.NUMBER, 50)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.DIVIDE), NumberNode(50)))

  ##
  # @brief Test parsing unary operations
  #
  def test_unary_operations(self):
    self.assertEqual(Parser([Token(TokenType.PLUS), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.PLUS), NumberNode(11)))
    self.assertEqual(Parser([Token(TokenType.MINUS), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.MINUS), NumberNode(11)))

  ##
  # @brief Test parsing keyword unary operations
  #
  def test_keyword_unary_operations(self):
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "abs"), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.KEYWORD, "abs"), NumberNode(11)))
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(11)))
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "ln"), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(11)))

  ##
  # @brief Test parsing valid operations with parentecies
  #
  def test_valid_parents(self):
    self.assertEqual(Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.PLUS), NumberNode(50)))

    self.assertEqual(Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN), Token(TokenType.PLUS), Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse(),
                     BinaryOperationNode(BinaryOperationNode(NumberNode(25), Token(TokenType.PLUS), NumberNode(50)), Token(TokenType.PLUS), BinaryOperationNode(NumberNode(25), Token(TokenType.PLUS), NumberNode(50))))

  ##
  # @brief Test parsing invalid operations with parentecies
  #
  def test_invalid_parents(self):
    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN), Token(TokenType.RPAREN)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.LPAREN), Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse()

  ##
  # @brief Test parsing complex operations and operations order
  #
  def test_operation_order(self):
    # ---5
    tokens = [
      Token(TokenType.MINUS),
      Token(TokenType.MINUS),
      Token(TokenType.MINUS),
      Token(TokenType.NUMBER, 5),
    ]
    self.assertEqual(str(Parser(tokens).parse()), "(MINUS, (MINUS, (MINUS, 5)))")

    # -e^255 / (2 * ln 3 - 8) + 16
    tokens = [
      Token(TokenType.MINUS),
      Token(TokenType.KEYWORD, "e"),
      Token(TokenType.POW),
      Token(TokenType.NUMBER, 255),
      Token(TokenType.DIVIDE),
      Token(TokenType.LPAREN),
      Token(TokenType.NUMBER, 2),
      Token(TokenType.MULTIPLY),
      Token(TokenType.KEYWORD, "ln"),
      Token(TokenType.NUMBER, 3),
      Token(TokenType.MINUS),
      Token(TokenType.NUMBER, 8),
      Token(TokenType.RPAREN),
      Token(TokenType.PLUS),
      Token(TokenType.NUMBER, 16),
    ]

    self.assertEqual(str(Parser(tokens).parse()), "(((MINUS, (2.718281828459045, POW, 255)), DIVIDE, ((2, MULTIPLY, (LN, 3)), MINUS, 8)), PLUS, 16)")

    # abs -15 + 30 * fact 2 * 3
    tokens = [
      Token(TokenType.KEYWORD, "abs"),
      Token(TokenType.NUMBER, -15),
      Token(TokenType.PLUS),
      Token(TokenType.NUMBER, 30),
      Token(TokenType.MULTIPLY),
      Token(TokenType.KEYWORD, "fact"),
      Token(TokenType.NUMBER, 2),
      Token(TokenType.MULTIPLY),
      Token(TokenType.NUMBER, 3),
    ]

    self.assertEqual(str(Parser(tokens).parse()), "((ABS, -15), PLUS, ((30, MULTIPLY, (FACT, 2)), MULTIPLY, 3))")

    # abs(-15 + 30) * fact 2 * 3
    tokens = [
      Token(TokenType.KEYWORD, "abs"),
      Token(TokenType.LPAREN),
      Token(TokenType.NUMBER, -15),
      Token(TokenType.PLUS),
      Token(TokenType.NUMBER, 30),
      Token(TokenType.RPAREN),
      Token(TokenType.MULTIPLY),
      Token(TokenType.KEYWORD, "fact"),
      Token(TokenType.NUMBER, 2),
      Token(TokenType.MULTIPLY),
      Token(TokenType.NUMBER, 3),
    ]

    self.assertEqual(str(Parser(tokens).parse()), "(((ABS, (-15, PLUS, 30)), MULTIPLY, (FACT, 2)), MULTIPLY, 3)")

  ##
  # @brief Test parsing invalid input with only operators
  #
  def test_only_operator_input(self):
    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.PLUS)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.MINUS)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.MULTIPLY)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.DIVIDE)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.POW)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.ROOT)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "abs")]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "ln")]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact")]).parse()

  def test_invalid_multi_operations(self):
    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.MULTIPLY), Token(TokenType.MULTIPLY), Token(TokenType.NUMBER, 10)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.DIVIDE), Token(TokenType.NUMBER, 10), Token(TokenType.MULTIPLY)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.NUMBER, 10), Token(TokenType.MULTIPLY), Token(TokenType.MULTIPLY), Token(TokenType.DIVIDE)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.POW), Token(TokenType.POW), Token(TokenType.NUMBER, 10)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.ROOT), Token(TokenType.NUMBER, 10), Token(TokenType.ROOT)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.NUMBER, 10), Token(TokenType.ROOT), Token(TokenType.POW), Token(TokenType.POW)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.MINUS), Token(TokenType.MINUS), Token(TokenType.NUMBER, 10), Token(TokenType.MINUS), Token(TokenType.POW), Token(TokenType.NUMBER, 10)]).parse()

  ##
  # @brief Test parsing unfinished expressions
  #
  def test_unfinished_expesions(self):
    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.PLUS)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.MINUS)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.MULTIPLY)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.DIVIDE)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.POW)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.ROOT)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.KEYWORD, "abs")]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.KEYWORD, "ln")]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.KEYWORD, "fact")]).parse()

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
