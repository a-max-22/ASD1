import unittest

from StackParenthesisBalanced import parenthesis_balanced


class TestParenthesisBalanced(unittest.TestCase):
    
    def test_empty(self):
        case = ''
        self.assertRaises(ValueError, parenthesis_balanced, case)
    
    def test_wrong_symbol(self):
        case = 's'        
        self.assertRaises(ValueError, parenthesis_balanced, case)
        
    def test_single(self):        
        self.assertFalse(parenthesis_balanced(')'))
        self.assertFalse(parenthesis_balanced('('))
    
    def test_balanced(self):
        self.assertTrue(parenthesis_balanced('()'))
        self.assertTrue(parenthesis_balanced('(())'))
        self.assertTrue(parenthesis_balanced('()()(())((()))'))
        self.assertTrue(parenthesis_balanced('()()(())((()))'))
    
    def test_unbalanced(self):
        self.assertFalse(parenthesis_balanced('(((((()'))
        self.assertFalse(parenthesis_balanced('(()))))'))
        self.assertFalse(parenthesis_balanced('(('))
        self.assertFalse(parenthesis_balanced('())('))
        self.assertFalse(parenthesis_balanced('))(('))
        self.assertFalse(parenthesis_balanced('((())'))
         