import unittest

from Queue import Queue
from QueueRotate import rotate_queue

def check_container(queue, expectedContainer):
    return queue.container == expectedContainer


class TestRotateQueue(unittest.TestCase):

    def test_rotate_empty(self):
        N = 17      
        rotationVal = 8
        expected = []
        actual = Queue()
        rotate_queue(actual, rotationVal)
        self.assertTrue(check_container(actual, []))
        self.assertEqual(actual.size(), 0)
    
    def test_rotate_req_queue(self):
        rotationVal = 8
        N = 17
        val = 2
        expected = [val]*(N - rotationVal) + [val+1]*rotationVal        
        actualContainer = [val+1]*rotationVal + [val]*(N - rotationVal)
        actual = Queue()
        actual.container = actualContainer
        rotate_queue(actual, rotationVal)
        self.assertEqual(actual.container, expected)
        self.assertEqual(actual.size(), N)