import unittest

from DequeCheckPalyndrom import *


class TestSize(unittest.TestCase):
    
    def test_empty(self):
        self.assertTrue(check_palyndrom(''))
    
    def test_even_palyndrom(self):
        self.assertTrue(check_palyndrom('p'))
        self.assertTrue(check_palyndrom('aa'))
        self.assertTrue(check_palyndrom('abba'))
        self.assertTrue(check_palyndrom('pabbap'))
        
    def test_non_even_palyndrom(self):
        self.assertTrue(check_palyndrom('aba'))
        self.assertTrue(check_palyndrom('abpba'))
        self.assertTrue(check_palyndrom('pabfbap'))
        
    def test_non_palyndrom(self):   
        self.assertFalse(check_palyndrom('abb'))
        self.assertFalse(check_palyndrom('bsbs'))
        self.assertFalse(check_palyndrom('bs'))