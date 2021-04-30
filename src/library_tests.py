##
# @package library_tests
#

import unittest
import math
from mathLib import MathFunctions, Interpreter, Parser, Tokenizer, Token, TokenType
from mathLib.basics.nodes import *
from mathLib.entry_point import interpret_text_input

##
# @brief Test mathematic operations of math library
#
class MathLibTestBasicFunctions(unittest.TestCase):
  ##
  # @brief add function tests
  #
  def test_add(self):  
    self.assertEqual(MathFunctions.add_operation(0, 1), 1)
    self.assertEqual(MathFunctions.add_operation(0, 0), 0)
    self.assertEqual(MathFunctions.add_operation(1, 0), 1)
    self.assertEqual(MathFunctions.add_operation(0, -1), -1)
    self.assertEqual(MathFunctions.add_operation(-1, 0), -1)
    self.assertEqual(MathFunctions.add_operation(1.5, 2.3), 3.8)
    self.assertEqual(MathFunctions.add_operation(100000, 900000), 1000000)
  ##
  # @brief subtraction function tests
  #
  def test_sub(self):  
    self.assertEqual(MathFunctions.sub_operation(1, 1), 0)
    self.assertEqual(MathFunctions.sub_operation(0, 1), -1)
    self.assertEqual(MathFunctions.sub_operation(1, 0), 1)
    self.assertAlmostEqual(MathFunctions.sub_operation(5.5, 4.3), 1.2)
    self.assertEqual(MathFunctions.sub_operation(-1, 1), -2)
    self.assertEqual(MathFunctions.sub_operation(5, -6), 11)
    self.assertAlmostEqual(MathFunctions.sub_operation(-5.3, -4.1), -1.2)
    self.assertEqual(MathFunctions.sub_operation(100, 5000000), -4999900)
  ##
  # @brief multiplication function tests
  #
  def test_mul(self):  
    self.assertEqual(MathFunctions.multiply_operation(1, 1), 1)
    self.assertEqual(MathFunctions.multiply_operation(1, 0), 0)
    self.assertEqual(MathFunctions.multiply_operation(0, 1), 0)
    self.assertEqual(MathFunctions.multiply_operation(5.3, 5), 26.5)
    self.assertEqual(MathFunctions.multiply_operation(1.2, 2.3), 2.76)
    self.assertEqual(MathFunctions.multiply_operation(12.345, 6.789), 83.810205)
    self.assertEqual(MathFunctions.multiply_operation(-5, 3), -15)
    self.assertEqual(MathFunctions.multiply_operation(-70, -33), 2310)
    self.assertEqual(MathFunctions.multiply_operation(-1450.1444, 789444784.8875), -1144808933913.812755)
  ##
  # @brief division function tests
  #
  def test_div(self):  
    self.assertEqual(MathFunctions.divide_operation(1, 1), 1)
    self.assertEqual(MathFunctions.divide_operation(0, 1), 0)
    self.assertEqual(MathFunctions.divide_operation(5, 5), 1)
    self.assertEqual(MathFunctions.divide_operation(10, 2), 5)
    self.assertEqual(MathFunctions.divide_operation(333, 111), 3)
    self.assertEqual(MathFunctions.divide_operation(15, 2), 7.5)
    self.assertEqual(MathFunctions.divide_operation(25, 4), 6.25)
    self.assertAlmostEqual(MathFunctions.divide_operation(159, 753), 0.21115537848, 10)
    self.assertAlmostEqual(MathFunctions.divide_operation(753, -159), -4.73584905660, 10)
  ##
  # @brief testing if division by 0 raises error
  #
  def test_div_by_zero(self):  
    with self.assertRaises(ZeroDivisionError):
      MathFunctions.divide_operation(0, 0)
    with self.assertRaises(ZeroDivisionError):
      MathFunctions.divide_operation(5, 0)
    with self.assertRaises(ZeroDivisionError):
      MathFunctions.divide_operation(-5, 0)
    with self.assertRaises(ZeroDivisionError):
      MathFunctions.divide_operation(-485.33, 0)

  ##
  # @brief power function tests
  #
  def test_pow(self):  
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

  ##
  # @brief root function tests
  #
  def test_root(self):  
    self.assertEqual(MathFunctions.root_operation(1, 1), 1)
    self.assertEqual(MathFunctions.root_operation(1, 5), 5)
    self.assertAlmostEqual(MathFunctions.root_operation(10, 5), 1.17461894308, 10)
    self.assertAlmostEqual(MathFunctions.root_operation(-5, 10), 0.63095734448, 10)
    self.assertAlmostEqual(MathFunctions.root_operation(16, 2), 1.04427378242, 10)
    self.assertAlmostEqual(MathFunctions.root_operation(12.5, 3), 1.09186689961, 10)
    self.assertAlmostEqual(MathFunctions.root_operation(1.2, 3.4), 2.77267583598, 10)
    self.assertAlmostEqual(MathFunctions.root_operation(-5.6, 7.8), 0.69294280921, 10)

  ##
  # @brief testing if root of negative numbers raises error
  #
  def test_root_of_neg_number(self):  
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(2, -5)
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(2, -5.5)
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(-4, -10)
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(-8.3, -5.778)

  ##
  # @brief testing if 0th root raises error
  #
  def test_zeroth_root(self):  
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(0, 1)
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(0, 5)
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(0, 55.5)

  ##
  # @brief natural logarithm function tests
  #
  def test_log(self):  
    self.assertEqual(MathFunctions.natural_log_operation(1), 0)
    self.assertAlmostEqual(MathFunctions.natural_log_operation(2), 0.69314718056, 10)
    self.assertAlmostEqual(MathFunctions.natural_log_operation(3.4), 1.22377543162, 10)
    self.assertAlmostEqual(MathFunctions.natural_log_operation(100), 4.60517018599, 10)
    self.assertAlmostEqual(MathFunctions.natural_log_operation(100100100100), 25.3294365233, 10)

  ##
  # @brief testing if natural logarithm of 0 raises error
  #
  def test_zero_log(self):  
    with self.assertRaises(RuntimeError):
      MathFunctions.natural_log_operation(0)

  ##
  # @brief testing if natural logarithm of negative numbers raises error
  #
  def test_neg_log(self):  
    with self.assertRaises(RuntimeError):
      MathFunctions.natural_log_operation(-1)
    with self.assertRaises(RuntimeError):
      MathFunctions.natural_log_operation(-13)
    with self.assertRaises(RuntimeError):
      MathFunctions.natural_log_operation(-45.44)

  ##
  # @brief factorial function tests
  #
  def test_fac(self):  
    self.assertEqual(MathFunctions.factorial_operation(0), 1)
    self.assertEqual(MathFunctions.factorial_operation(1), 1)
    self.assertEqual(MathFunctions.factorial_operation(5), 120)
    self.assertEqual(MathFunctions.factorial_operation(10), 3628800)

  ##
  # @brief testing if factorial of non intiger numbers (float, double) raises error
  #
  def test_non_intiger_fac(self):  
    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(1.1)
    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(5.7)
    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(435.854)

  ##
  # @brief testing if factorial of negative numbers raises error
  #
  def test_neg_number_fac(self):  
    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(-1)
    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(-5)
    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(-8.3)

  ##
  # @brief inversion function tests
  #
  def test_inv(self):  
    self.assertEqual(MathFunctions.invert_operation(0), 0)
    self.assertEqual(MathFunctions.invert_operation(1), -1)
    self.assertEqual(MathFunctions.invert_operation(-1), 1)
    self.assertEqual(MathFunctions.invert_operation(50), -50)
    self.assertEqual(MathFunctions.invert_operation(-100.25), 100.25)

  ##
  # @brief absolute value function tests
  #
  def test_abs(self): 
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
    self.assertEqual(Tokenizer("e").tokenize(), [Token(TokenType.KEYWORD, "e")])
    self.assertEqual(Tokenizer("abs").tokenize(), [Token(TokenType.KEYWORD, "abs")])
    self.assertEqual(Tokenizer("ln").tokenize(), [Token(TokenType.KEYWORD, "ln")])
    self.assertEqual(Tokenizer("fact").tokenize(), [Token(TokenType.KEYWORD, "fact")])
    self.assertEqual(Tokenizer("rand").tokenize(), [Token(TokenType.KEYWORD, "rand")])
    self.assertEqual(Tokenizer("abs fact ln").tokenize(), [
      Token(TokenType.KEYWORD, "abs"),
      Token(TokenType.KEYWORD, "fact"),
      Token(TokenType.KEYWORD, "ln")
    ])
  
  ##
  # @brief Test combined expression
  #
  def test_combined_expression(self):
    self.assertEqual(Tokenizer("abs( 10.01 ^(9/ 3)- 15\n*ln(e* e)) +rand*2.5\t +3√18- 654321 \n*fact(4.)+.15").tokenize(), [
      Token(TokenType.KEYWORD, "abs"),
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
      Token(TokenType.KEYWORD, "ln"),
      Token(TokenType.LPAREN),
      Token(TokenType.KEYWORD, "e"),
      Token(TokenType.MULTIPLY),
      Token(TokenType.KEYWORD, "e"),
      Token(TokenType.RPAREN),
      Token(TokenType.RPAREN),
      Token(TokenType.PLUS),
      Token(TokenType.KEYWORD, "rand"),
      Token(TokenType.MULTIPLY),
      Token(TokenType.NUMBER, 2.5),
      Token(TokenType.PLUS),
      Token(TokenType.NUMBER, 3),
      Token(TokenType.ROOT),
      Token(TokenType.NUMBER, 18),
      Token(TokenType.MINUS),
      Token(TokenType.NUMBER, 654321),
      Token(TokenType.MULTIPLY),
      Token(TokenType.KEYWORD, "fact"),
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

  ##
  # @brief Test invalid operations on parser
  #
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
  def setUp(self) -> None:
    self.interpreter = Interpreter()

  ##
  # @brief Testing interpretation of single numbers
  #   
  def test_numbers(self):
    self.assertEqual(self.interpreter.interpret(NumberNode(0)).get_value(), 0)
    self.assertEqual(self.interpreter.interpret(NumberNode(5)).get_value(), 5)
    self.assertEqual(self.interpreter.interpret(NumberNode(-5)).get_value(), -5)
    self.assertEqual(self.interpreter.interpret(NumberNode(-5.5)).get_value(), -5.5)
    self.assertEqual(self.interpreter.interpret(NumberNode(5555555555)).get_value(), 5555555555)

  ##
  # @brief Testing interpretation of unary operations
  #
  def test_unary(self):
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.PLUS), NumberNode(6))).get_value(), 6)
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.MINUS), NumberNode(6))).get_value(), -6)
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.PLUS), NumberNode(-7.5))).get_value(), -7.5)
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.MINUS), NumberNode(-8.6))).get_value(), 8.6)
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "abs"), NumberNode(15))).get_value(), 15)
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "abs"), NumberNode(-33.3))).get_value(), 33.3)
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(5))).get_value(), 120)
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(10))).get_value(), 3628800)
    self.assertAlmostEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(10))).get_value(), 2.30258509299, 10)
    self.assertAlmostEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(15.6))).get_value(), 2.74727091426, 10)
  
  ##
  # @brief Testing interpretation of binary operations
  #
  def test_binary(self):
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(1), Token(TokenType.PLUS), NumberNode(1))).get_value(), 2)
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(71.3), Token(TokenType.PLUS), NumberNode(28.7))).get_value(), 100)
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(10), Token(TokenType.MINUS), NumberNode(15))).get_value(), -5)
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(15), Token(TokenType.MINUS), NumberNode(10))).get_value(), 5)
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(10), Token(TokenType.DIVIDE), NumberNode(5))).get_value(), 2)
    self.assertAlmostEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(55), Token(TokenType.DIVIDE), NumberNode(43))).get_value(), 1.27906976744, 10)
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(3), Token(TokenType.MULTIPLY), NumberNode(4))).get_value(), 12)
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(0), Token(TokenType.MULTIPLY), NumberNode(6000))).get_value(), 0)
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(3), Token(TokenType.POW), NumberNode(0))).get_value(), 1)
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(2), Token(TokenType.POW), NumberNode(10))).get_value(), 1024)
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(2), Token(TokenType.ROOT), NumberNode(4))).get_value(), 2)
    self.assertAlmostEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(3), Token(TokenType.ROOT), NumberNode(5))).get_value(), 1.70997594668, 10)
  
  ##
  # @brief Testing if interpretation of invalid function inputs raises error
  #
  def test_invalid_inputs(self):
    with self.assertRaises(ZeroDivisionError):
      self.interpreter.interpret(BinaryOperationNode(NumberNode(10), Token(TokenType.DIVIDE), NumberNode(0)))
    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(BinaryOperationNode(NumberNode(0), Token(TokenType.ROOT), NumberNode(15)))
    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(BinaryOperationNode(NumberNode(2), Token(TokenType.ROOT), NumberNode(-3)))
    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(1.1)))
    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(-1)))
    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(0)))
    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(-1)))




##
# @brief Testing entrypoint for UI
#
class MathLibTestExpressions(unittest.TestCase):

  ##
  # @brief testing interpretation of add function
  #
  def test_int_add(self):
    self.assertEqual(interpret_text_input("0 + 0"),  "0")
    self.assertEqual(interpret_text_input("10 + 5"),  "15")
    self.assertEqual(interpret_text_input("10.5 + 5.35"),  "15.85")
    self.assertEqual(interpret_text_input("485.477 + 7741.999"),  "8227.476")
  
  ##
  # @brief testing interpretation of subtraction function
  #
  def test_int_sub(self):
    self.assertEqual(interpret_text_input("0 - 0"), "0")
    self.assertEqual(interpret_text_input("5 - 4"), "1")
    self.assertEqual(interpret_text_input("4 - 5"), "-1")
    self.assertEqual(interpret_text_input("15.2 - 16.2"), "-1")
    self.assertAlmostEqual(float(interpret_text_input("7855.445 - 889.51")), 6965.9349999999995)
  
  ##
  # @brief testing interpretation of multiply function
  #
  def test_int_mul(self):
    self.assertEqual(interpret_text_input("0 * 0"), "0")
    self.assertEqual(interpret_text_input("5 * 0"), "0")
    self.assertEqual(interpret_text_input("7 * 8"), "56")
    self.assertEqual(interpret_text_input("33.5 * 74.4"), "2492.4")
    self.assertEqual(interpret_text_input("456.789 * 987.654"), "451149.483006")
  
  ##
  # @brief testing interpretation of division function
  #
  def test_int_div(self):
    self.assertEqual(interpret_text_input("0 / 5"), "0")
    self.assertEqual(interpret_text_input("5 / 5"), "1")
    self.assertEqual(interpret_text_input("14 / 5"), "2.8")
    self.assertAlmostEqual(float(interpret_text_input("45.3 / 56")), float("0.8089285714"), 9)
  
  ##
  # @brief testing interpretation of power function
  #
  def test_int_pow(self):
    self.assertEqual(interpret_text_input("1^0"), "1")
    self.assertEqual(interpret_text_input("2^1"), "2")
    self.assertEqual(interpret_text_input("5^6"), "15625")
    self.assertAlmostEqual(float(interpret_text_input("4.5^5.6")), 4549.77664599199)
    self.assertAlmostEqual(float(interpret_text_input("451.1^2.4")), 2345604.49398618945)
  
  ##
  # @brief testing interpretation of root function
  #
  def test_int_root(self):
    self.assertEqual(interpret_text_input("1√5"), "5")
    self.assertAlmostEqual(float(interpret_text_input("2√5")), 2.2360679774)
    self.assertAlmostEqual(float(interpret_text_input("5√5")), 1.37972966146)
    self.assertAlmostEqual(float(interpret_text_input("15√452.45")), 1.50327363084)
  
  ##
  # @brief testing interpretation of natural logarithm function
  #
  def test_int_ln(self):
    self.assertEqual(interpret_text_input("ln 1"), "0")
    self.assertAlmostEqual(float(interpret_text_input("ln 5")), 1.60943791243, 10)
    self.assertAlmostEqual(float(interpret_text_input("ln 5.3")), 1.66770682055, 10)
    self.assertAlmostEqual(float(interpret_text_input("ln 789.789")), 6.67176582117, 10)

  ##
  # @brief testing interpretation of absolute value function
  #
  def test_int_abs(self):
    self.assertEqual(interpret_text_input("abs 0"), "0")
    self.assertEqual(interpret_text_input("abs 1"), "1")
    self.assertEqual(interpret_text_input("abs -1"), "1")
    self.assertEqual(interpret_text_input("abs -485.756"), "485.756")
  ##
  # @brief testing interpretation of factorial function
  #
  def test_int_fact(self):
    self.assertEqual(interpret_text_input("fact 1"), "1")
    self.assertEqual(interpret_text_input("fact 2"), "2")
    self.assertEqual(interpret_text_input("fact 5"), "120")
    self.assertEqual(interpret_text_input("fact 13"), "6227020800")
  
  ##
  # @brief testing interpretation of multiple functions
  #
  def test_int_multiple(self):
    self.assertAlmostEqual(float(interpret_text_input("5 + 5 - 4 / 6 + 8 * 4")), 41.33333333333)
    self.assertEqual(float(interpret_text_input("abs -5^5 - 4 / 6√8 * fact 4")), 3057.1177490060913)
  
  ##
  # @brief testing violating mathematical rules 
  #
  def test_int_violation(self):
    self.assertEqual(interpret_text_input("4 / 0"), "Error")
    self.assertEqual(interpret_text_input("0√10"), "Error")
    self.assertEqual(interpret_text_input("2√-78"), "Error")
    self.assertEqual(interpret_text_input("fact -5"), "Error")
    self.assertEqual(interpret_text_input("fact 55.5"), "Error")
    self.assertEqual(interpret_text_input("ln 0"), "Error")
    self.assertEqual(interpret_text_input("ln -30"), "Error")
  ##
  # @brief testing syntax
  #
  def test_int_syntax(self):
    self.assertEqual(interpret_text_input("qqqqqqqqqqqqqq"), "Error")
    self.assertEqual(interpret_text_input("5////////4"), "Error")
    self.assertEqual(interpret_text_input("14a+sa"), "Error")
    self.assertEqual(interpret_text_input("())fact (5)1(((asd)"), "Error")
    self.assertEqual(interpret_text_input("fact ln abs √^+-/*"), "Error")

if __name__ == '__main__':
  try:
    unittest.main()
  except Exception as e:
    print(f"Compiling of test failed\n{e}")
