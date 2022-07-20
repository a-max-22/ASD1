import unittest

from QueueViaStack import Queue

def check_stack(stack, expectedContainer):
    return stack.stack == expectedContainer

def make_stack_from_list(lst):
    result = Stack()
    result.stack = lst
    return result

def enqueue_list(queue, lst):
    for l in lst:
        queue.enqueue(l)

def dequeue_elems(queue, n):
    res = []
    for i in range(0,n):
        res.append(queue.dequeue())
    return res
    
    
class TestEnqueue(unittest.TestCase):

    def test_enqueue_empty(self):
        val = 17
        expected = [val]
        actual = Queue()
        actual.enqueue(val)
        self.assertTrue(check_stack(actual.enqStack, expected))        
        self.assertTrue(check_stack(actual.deqStack, []))                
        self.assertEqual(actual.size(), 1)

    def test_enqueue_non_empty(self):
        N = 17                
        actualElems = [x for x in range(0,N)]
        
        actual = Queue()
        enqueue_list(actual, actualElems)        
        
        self.assertEqual(actual.size(), N)
        self.assertTrue(check_stack(actual.enqStack, actualElems[::-1]))        
        self.assertTrue(check_stack(actual.deqStack, []))                


class TestDequeue(unittest.TestCase):
    
    def test_dequeue_empty(self):
        actual = Queue()
        val = actual.dequeue()
        self.assertTrue(check_stack(actual.enqStack, []))        
        self.assertTrue(check_stack(actual.deqStack, []))                
        self.assertEqual(actual.size(), 0)
        self.assertTrue(val is None)
        
    def test_dequeue_single(self):
        N = 28
        actual = Queue()        
        actual.enqueue(N)
        val = actual.dequeue()
        
        self.assertTrue(check_stack(actual.enqStack, []))        
        self.assertTrue(check_stack(actual.deqStack, []))                
        self.assertEqual(actual.size(), 0)
        self.assertEqual(val, N)

    def test_dequeue_non_single(self):
        N = 17                
        actualElems = [x for x in range(0,N)]
        
        actual = Queue()
        enqueue_list(actual, actualElems)
        val = actual.dequeue()
        
        self.assertEqual(val, 0)
        self.assertEqual(actual.size(), N-1)
        self.assertTrue(check_stack(actual.enqStack, []))        
        self.assertTrue(check_stack(actual.deqStack, actualElems[1:]))                

class TestState(unittest.TestCase):
    
    def test_internal_stacks(self):
        totalCount = 17
        part1 = 4
        deqNum1 = part1 - 2
        part2 = 5
        deqNum2 = part2 - 1
        
        actualElems = [x for x in range(0, totalCount)]        
        queue = Queue()
        
        enqueue_list(queue, actualElems[0:part1])
        deqLst = dequeue_elems(queue, deqNum1)        
        self.assertEqual(queue.size(), part1 - deqNum1)
        self.assertTrue(check_stack(queue.enqStack, []))        
        self.assertTrue(check_stack(queue.deqStack, actualElems[deqNum1:part1]))
        
        enqueue_list(queue, actualElems[part1:part1 + part2])

        self.assertEqual(queue.size(), part1 + part2 - deqNum1)        
        self.assertTrue(check_stack(queue.enqStack, actualElems[part1+part2-1:part1-1:-1]))
        self.assertTrue(check_stack(queue.deqStack, actualElems[deqNum1:part1]))
        self.assertEqual(deqLst, actualElems[0: deqNum1])
        
        deqLst = dequeue_elems(queue, deqNum2)                
        self.assertEqual(queue.size(), part1 + part2 - (deqNum1 + deqNum2))
        self.assertTrue(check_stack(queue.enqStack,[]))
        self.assertTrue(check_stack(queue.deqStack,actualElems[deqNum1+deqNum2:part1+part2]))
        self.assertEqual(deqLst, actualElems[deqNum1: deqNum1+deqNum2])        