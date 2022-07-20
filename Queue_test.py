import unittest

from Queue import Queue

def check_container(queue, expectedContainer):
    return queue.container == expectedContainer



class TestEnqueue(unittest.TestCase):

    def test_enqueue_empty(self):
        val = 17
        expected = [val]
        actual = Queue()
        actual.enqueue(val)
        self.assertTrue(check_container(actual, expected))
        self.assertEqual(actual.size(), 1)

    def test_enqueue_non_empty(self):
        N = 17        
        expected = [x for x in range(0,N+1)]
        actualContainer = [x for x in range(0,N)]
        actual = Queue()       
        actual.container = actualContainer        
        actual.enqueue(N)
        self.assertTrue(check_container(actual, expected))
        self.assertEqual(actual.size(), N+1)
    
class TestDequeue(unittest.TestCase):
    
    def test_dequeue_empty(self):
        actual = Queue()
        val = actual.dequeue()
        self.assertTrue(check_container(actual, []))
        self.assertEqual(actual.size(), 0)
        self.assertTrue(val is None)
        
    def test_dequeue_single(self):
        N = 28
        actual = Queue()
        actual.container = [N]
        val = actual.dequeue()
        self.assertTrue(check_container(actual, []))
        self.assertEqual(actual.size(), 0)
        self.assertEqual(val, N)
        
    def test_dequeue_non_single(self):
        N = 28
        expected = [x for x in range(1,N)]
        actual = Queue()
        actual.container = [x for x in range(0,N)]
        
        val = actual.dequeue()
        self.assertTrue(check_container(actual, expected))
        self.assertEqual(actual.size(), N-1)
        self.assertEqual(val, 0)
        
class TestSize(unittest.TestCase):
    
    def test_size_empty(self):
        actual = Queue()
        actual.container = []
        self.assertEqual(actual.size(), 0)
    
    def test_size_non_empty(self):
        N = 18
        actual = Queue()
        actual.container = [x for x in range(0,N)]
        self.assertEqual(actual.size(), N)
