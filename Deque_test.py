import unittest

from Deque import Deque

def check_container(deque, expectedContainer):
    return deque.container == expectedContainer

def set_container(deque, container):
    deque.container = container


class TestSize(unittest.TestCase):
    
    def test_size_empty(self):
        actual = Deque()        
        self.assertEqual(actual.size(), 0)
    
    def test_size_non_empty(self):
        N = 18
        actual = Deque()
        set_container(actual, [x for x in range(0,N)])        
        self.assertEqual(actual.size(), N)


class TestAddFront(unittest.TestCase):

    def test_add_empty(self):
        val = 17
        expected = [val]
        actual = Deque()
        actual.addFront(val)
        self.assertTrue(check_container(actual, expected))
        self.assertEqual(actual.size(), 1)

    def test_add_non_empty(self):
        N = 17        
        expected = [N]+[x for x in range(1,N)]
        actualContainer = [x for x in range(1,N)]
        actual = Deque()
        set_container(actual, actualContainer)
        actual.addFront(N)
        self.assertTrue(check_container(actual, expected))
        self.assertEqual(actual.size(), N)


class TestAddTail(unittest.TestCase):
    
    def test_add_empty(self):
        val = 17
        expected = [val]
        actual = Deque()
        actual.addTail(val)
        self.assertTrue(check_container(actual, expected))
        self.assertEqual(actual.size(), 1)

    def test_add_non_empty(self):
        N = 17        
        actualContainer = [x for x in range(N)]
        expected = [x for x in range(N+1)]
        actual = Deque()
        set_container(actual, actualContainer)
        actual.addTail(N)
        self.assertTrue(check_container(actual, expected))
        self.assertEqual(actual.size(), N+1)

class TestRemoveFront(unittest.TestCase):
    
    def test_remove_empty(self):
        N = 19
        val = 17
        expected = []
        actual = Deque()
        val = actual.removeFront()
        self.assertTrue(check_container(actual, expected))
        self.assertEqual(actual.size(), 0)
        self.assertTrue(val is None)
        
    def test_remove_single(self):
        N = 24        
        expected = []
        actual = Deque()
        set_container(actual, [N])
        val = actual.removeFront()
        self.assertTrue(check_container(actual, expected))
        self.assertEqual(actual.size(), 0)
        self.assertEqual(val, N)

    def test_remove_from_multiple_elem_deque(self):
        N = 21
        expected = [x for x in range(1,N)]
        actualContainer = [x for x in range(0,N)]
        actual = Deque()
        set_container(actual, actualContainer)
        val = actual.removeFront()
        self.assertTrue(check_container(actual, expected))
        self.assertEqual(actual.size(), N-1)
        self.assertEqual(val, 0)


class TestRemoveTail(unittest.TestCase):    
    def test_remove_empty(self):
        N = 33        
        expected = []
        actual = Deque()
        val = actual.removeTail()
        self.assertTrue(check_container(actual, expected))
        self.assertEqual(actual.size(), 0)
        self.assertTrue(val is None)
        
    def test_remove_single(self):
        N = 24        
        expected = []
        actual = Deque()
        set_container(actual, [N])
        val = actual.removeTail()
        self.assertTrue(check_container(actual, expected))
        self.assertEqual(actual.size(), 0)
        self.assertEqual(val, N)


    def test_remove_from_multiple_elem_deque(self):
        N = 21
        expected = [x for x in range(N-1)]
        actualContainer = [x for x in range(N)]
        actual = Deque()
        set_container(actual, actualContainer)
        val = actual.removeTail()
        self.assertTrue(check_container(actual, expected))
        self.assertEqual(actual.size(), N-1)
        self.assertEqual(val, N-1)
