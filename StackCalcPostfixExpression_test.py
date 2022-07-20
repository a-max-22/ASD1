import unittest

from StackCalcPostfixExpression import calc_postfix_expression

class TestStackCalcPostfixExpression(unittest.TestCase):

    def test_correct_expression(self):
        self.assertEqual(calc_postfix_expression('1 2 +'), 3)
        self.assertEqual(calc_postfix_expression('2 2 *'), 4)
        self.assertEqual(calc_postfix_expression('8 2 + 5 * 9 + ='), 59)
        self.assertEqual(calc_postfix_expression('1 ='), 1)
        self.assertEqual(calc_postfix_expression('1 2 + = 5'), 3)
        self.assertEqual(calc_postfix_expression('122323 1 + ='), 122324)
        self.assertEqual(calc_postfix_expression('1 2 3 4 + ='), 7)

    def test_incorrect_expression(self):
        self.assertRaises(ValueError, calc_postfix_expression, '=')
        self.assertRaises(ValueError, calc_postfix_expression, '5 2 * +')
        self.assertRaises(ValueError, calc_postfix_expression, '5 2 * ;')
        self.assertRaises(ValueError, calc_postfix_expression, '5 2 * sds')
        self.assertRaises(ValueError, calc_postfix_expression, '5 + 2 =')
