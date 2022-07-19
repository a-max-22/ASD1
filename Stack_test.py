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
        self.assertEqual(actual.size(), 1)
    
    def test_push_nonempty(self):        
        N = 16
        expected = [N]+[x for x in range(0, N)]
        actualContainer = [x for x in range(0, N)]        
        actual = Stack()
        actual.stack = actualContainer       
        actual.push(N)
        self.assertTrue(check_stack(actual, expected))
        self.assertEqual(actual.size(), N+1)


    def test_push_to_one_elem_stack(self):        
        N = 16
        expected = [N]
        actual = Stack()
        actual.push(N)
        self.assertTrue(check_stack(actual, expected))
        self.assertEqual(actual.size(), 1)


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
        self.assertEqual(actual.size(), 0)
    
    def test_pop_non_last_non_empty(self):
        N = 17
        expected = [x for x in range(1,N)]
        actualContainer = [x for x in range(0,N)]
        actual = Stack()
        actual.stack = actualContainer
        val = actual.pop()
        self.assertTrue(check_stack(actual, expected))
        self.assertEqual(val, 0)
        self.assertEqual(actual.size(), N-1)

class TestPeek(unittest.TestCase):

    def test_peek_empty(self):
        expected = []
        actual = Stack()
        val = actual.peek()
        self.assertTrue(check_stack(actual, expected))
        self.assertTrue(val is None)
        self.assertEqual(actual.size(), 0)
    
    def test_peek_nonempty(self):
        N = 18
        expected = [x for x in range(0,N+1)]
        actualContainer = [x for x in range(0,N+1)]
        actual = Stack()
        actual.stack = actualContainer
        val = actual.peek()
        self.assertTrue(check_stack(actual, expected))
        self.assertEqual(val, 0)
        self.assertEqual(actual.size(), N+1)


class TestSize(unittest.TestCase):
    
    def test_size_empty(self):
        actual = Stack()
        self.assertEqual(actual.size(), 0)
        
    def test_size_non_empty(self):
        N = 18
        actualContainer = [x for x in range(0,N)]
        actual = Stack()
        actual.stack = actualContainer                
        self.assertEqual(actual.size(), N)
        