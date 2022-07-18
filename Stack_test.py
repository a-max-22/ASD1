import unittest

from Stack import Stack

def check_stack(stack, expectedContainer):
    return stack.stack == expectedContainer


class TestPush(unittest.TestCase):

    def test_push_empty(self):
        val = 17
        expected = [val]
        actual = Stack()        
        actual.push(val)
        self.assertTrue(check_stack(actual, expected))
    
    def test_push_nonempty(self):        
        N = 16
        expected = [x for x in range(0, N+1)]
        actualContainer = [x for x in range(0, N)]        
        actual = Stack()
        actual.stack = actualContainer       
        actual.push(N)
        self.assertTrue(check_stack(actual, expected))

    def test_push_to_one_elem_stack(self):        
        N = 16
        expected = [N]
        actual = Stack()
        actual.push(N)
        self.assertTrue(check_stack(actual, expected))        


class TestPop(unittest.TestCase):

    def test_pop_empty(self):
        expected = []
        actual = Stack()
        val = actual.pop()
        self.assertTrue(check_stack(actual, expected))
        self.assertTrue(val is None)
        
    def test_pop_last(self):                    
        N = 16
        expected = []
        actualContainer = [N]
        actual = Stack()
        actual.stack = actualContainer
        val = actual.pop()
        self.assertTrue(check_stack(actual, expected))
        self.assertEqual(val, N)
    
    def test_pop_non_last_non_empty(self):
        N = 17
        expected = [x for x in range(0,N)]
        actualContainer = [x for x in range(0,N+1)]
        actual = Stack()
        actual.stack = actualContainer
        val = actual.pop()
        self.assertTrue(check_stack(actual, expected))
        self.assertEqual(val, N)

class TestPeek(unittest.TestCase):

    def test_peek_empty(self):
        expected = []
        actual = Stack()
        val = actual.peek()
        self.assertTrue(check_stack(actual, expected))
        self.assertTrue(val is None)
    
    def test_peek_nonempty(self):
        N = 18
        expected = [x for x in range(0,N+1)]
        actualContainer = [x for x in range(0,N+1)]
        actual = Stack()
        actual.stack = actualContainer
        val = actual.peek()
        self.assertTrue(check_stack(actual, expected))
        self.assertEqual(val, N)
