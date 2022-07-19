import unittest
from LinkedList2DummyNode import LinkedList2, Node, DummyNode


def make_linked_list(initialList):        
    result = LinkedList2()
    for val in initialList:
        result.add_in_tail(Node(val))            
    return result

def get_n_th_node(linkedList, n):
    node = linkedList.head()
    prev = None
    i = 0
    while not linkedList.is_past_end(node) and i < n:
        i += 1
        node = node.next        
    return node
    
def get_linked_list_nodes_by_indexes(linkedList, indexes):
    result = []
    for i in indexes:
        node = get_n_th_node(linkedList, i)
        if node is not None:
            result.append(node)
    return result


def print_nodes(linkedList):
    node = linkedList.head()
    while not linkedList.is_past_end(node):
        print(node.value)
        node = node.next
    

class TestEquality(unittest.TestCase):

    def test_empty_equals_empty(self):
        emptyList1 = LinkedList2()
        emptyList2 = LinkedList2()
        self.assertEqual(emptyList1, emptyList2)

    def test_empty_neq_non_empty(self):
        emptyList = LinkedList2()
        nonEmptyList = make_linked_list([1,2,3])
        singleElemList = make_linked_list([1])        
        self.assertFalse(emptyList == nonEmptyList)
        self.assertFalse(emptyList == singleElemList)

    def test_eq_size_one(self):
        list1 = make_linked_list([1])
        list2 = make_linked_list([1])
        self.assertEqual(list1, list2)

    def test_neq_size_one(self):
        list1 = make_linked_list([1])
        list2 = make_linked_list([2])
        self.assertFalse(list1 == list2)
    
    def test_eq_size_n(self):
        list1 = make_linked_list([1,2,3,4,5,6,7,8,9,10,11,12])
        list2 = make_linked_list([1,2,3,4,5,6,7,8,9,10,11,12])
        list3 = make_linked_list([1,2,3,4,5,6,7,8,9,10,11,0])
        list4 = make_linked_list([0,2,3,4,5,6,7,8,9,10,11,12])
        self.assertEqual(list1, list2)
        self.assertFalse(list1 == list3)
        self.assertFalse(list1 == list4)
    
    def test_diff_size_lists(self):
        list1 = make_linked_list([1,2,3,4,5,6,7,8,9,10,11,12])
        list2 = make_linked_list([1,2,3,4,5,6,7,8])
        list3 = make_linked_list([8,9,10,11,12])
        self.assertFalse(list1 == list2)
        self.assertFalse(list2 == list3)

class TestFind(unittest.TestCase):
    
    def test_find(self):
        valueToFind = 3
        valueToFindPos = 4
        numRemainedElements = 5
        regList  = [valueToFind+1] * valueToFindPos + [valueToFind] + [valueToFind+2] *numRemainedElements
        
        linkedList = make_linked_list(regList)
        head,tail = linkedList.head(), linkedList.tail() 
        
        self.assertEqual(linkedList.find(valueToFind), get_n_th_node(linkedList, valueToFindPos))
        self.assertEqual((head,tail), (linkedList.head(), linkedList.tail()))

    def test_find_in_head(self):
        valueToFind = 3
        N = 5
        regList = [valueToFind] + [valueToFind+1] * N + [valueToFind] * N
        
        linkedList = make_linked_list(regList)
        head,tail = linkedList.head(), linkedList.tail()
        
        self.assertEqual(linkedList.find(valueToFind), linkedList.head())
        self.assertEqual((head,tail), (linkedList.head(), linkedList.tail()))
        
    def test_find_in_tail(self):
        valueToFind = 3
        N = 5
        regList = [valueToFind+1] * N + [valueToFind]
        
        linkedList = make_linked_list(regList)
        head,tail = linkedList.head(), linkedList.tail()
        
        self.assertEqual(linkedList.find(valueToFind), linkedList.tail())
        self.assertEqual((head,tail), (linkedList.head(), linkedList.tail()))


    def test_find_absent(self):
        valueToFind = 3
        numElements = 17
        regList  = [valueToFind+2] * numElements
        
        linkedList = make_linked_list(regList)
        head,tail = linkedList.head(), linkedList.tail()
        
        self.assertEqual(linkedList.find(valueToFind), None)
        self.assertEqual((head,tail), (linkedList.head(), linkedList.tail()))

    def test_find_if_multiple_values(self):
        valueToFind = 3
        N = 5
        regList = [valueToFind + 1] + [valueToFind]*N + [valueToFind+1]*N + [valueToFind] * N
        
        linkedList = make_linked_list(regList)
        head,tail = linkedList.head(), linkedList.tail()
        
        self.assertEqual(linkedList.find(valueToFind), get_n_th_node(linkedList, 1))
        self.assertEqual((head,tail), (linkedList.head(), linkedList.tail()))

    
    def test_find_in_empty_list(self):
        valueToFind = 3
        linkedList = LinkedList2()
        head,tail = None, None
        
        self.assertEqual(linkedList.find(valueToFind),  None)
        self.assertEqual(None, None)

class TestFind(unittest.TestCase):
    
    def test_find_in_empty_list(self):
        valueToFind = 3
        linkedList = LinkedList2()
        head,tail = linkedList.head(), linkedList.tail()
        
        self.assertEqual(linkedList.find_all(valueToFind), [])
        self.assertEqual((head,tail), (linkedList.head(), linkedList.tail()))
        
    def test_find_absent_element(self):
        valueToFind = 3
        numElements = 17
        regList     = [valueToFind+2] * numElements
        
        linkedList = make_linked_list(regList)
        head, tail = linkedList.head(), linkedList.tail()
        
        self.assertEqual(linkedList.find_all(valueToFind), [])
        self.assertEqual((head,tail), (linkedList.head(), linkedList.tail()))


    def test_find_single(self):
        val = 3
        N = 6
        regList = [val+1]* N + [val] + [val+2]*2*N
        regList2 = [val] + [val+2]*2*N
        regList3 = [val+2]*2*N + [val]

        linkedList = make_linked_list(regList)
        linkedList2 = make_linked_list(regList2)
        linkedList3 = make_linked_list(regList3)

        head,tail = linkedList.head(), linkedList.tail() 
        head2,tail2 = linkedList2.head(), linkedList2.tail() 
        head3,tail3 = linkedList3.head(), linkedList3.tail() 
        
        self.assertEqual(linkedList.find_all(val), [get_n_th_node(linkedList, N)])
        self.assertEqual((head,tail), (linkedList.head(), linkedList.tail()))

        self.assertEqual(linkedList2.find_all(val), [linkedList2.head()])
        self.assertEqual((head2,tail2), (linkedList2.head(), linkedList2.tail()))

        self.assertEqual(linkedList3.find_all(val),  [linkedList3.tail()])       
        self.assertEqual((head3,tail3), (linkedList3.head(), linkedList3.tail()))
        

    def test_find_multiple(self):
        val = 3
        regList = [val]*2 + [val+1]*3 + [val]*2 + [val+2]*4 + [val]*2

        linkedList = make_linked_list(regList)
        head,tail  = linkedList.head(), linkedList.tail()
        expectedList = get_linked_list_nodes_by_indexes(linkedList, [0,1,5,6,11,12])

        self.assertEqual(linkedList.find_all(val), expectedList)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))


class TestDeleteOne(unittest.TestCase):
    
    def test_delete_from_empty_list(self):
        val = 3
        linkedList = LinkedList2()
        head,tail  = linkedList.head(), linkedList.tail()

        linkedList.delete(val, all=False)

        self.assertEqual(linkedList, LinkedList2())
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))


    def test_delete_absent_elem(self):
        val = 3
        numElements = 17
        regList  = [val+2] * numElements

        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList)
        head,tail  = linkedList.head(), linkedList.tail()

        linkedList.delete(val, all=False)

        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))


    def test_delete_elem(self):
        val = 3
        N = 17
        
        regList  = [val+2]*N + [val] + [val+2]*2*N
        regList2  = [val+2]*N + [val+2]*2*N

        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList2)
        head,tail  = linkedList.head(), linkedList.tail()

        linkedList.delete(val, all=False)

        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))


    def test_delete_head(self):
        val = 3
        N = 17
        
        regList  = [val]*2 + [val+2]*2*N
        regList2  = [val] + [val+2]*2*N

        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList2)
        head,tail  = linkedList.head().next, linkedList.tail()

        linkedList.delete(val, all=False)

        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))


    def test_delete_tail(self):
        val = 3
        N = 17
        
        regList  =  [val+2]*N + [val]
        regList2  = [val+2]*N

        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList2)
        head,tail  = linkedList.head(), linkedList.tail().prev

        linkedList.delete(val, all=False)

        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))


    def test_delete_all_elements(self):
        val = 3
        
        regList  =  [val]

        linkedList = make_linked_list(regList)
        expectedLinkedList = LinkedList2()
        head,tail  = linkedList.dummyTail, linkedList.dummyHead
        
        linkedList.delete(val, all=False)

        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))

    def test_delete_only_first_value(self):
        val = 3
        N = 20
        regList = [val]*N
        regList2 = [val]*(N-1)
        
        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList2)
        head,tail  = linkedList.head().next, linkedList.tail()

        linkedList.delete(val, all=False)

        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))
        

class TestDeleteAll(unittest.TestCase):
    
    def test_delete_from_empty_list(self):
        val = 3
        linkedList = LinkedList2()
        head,tail  = linkedList.head(), linkedList.tail()

        linkedList.delete(val, all=True)

        self.assertEqual(linkedList, LinkedList2())
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))
    
    def test_delete_absent_elem(self):
        val = 3
        numElements = 17
        regList  = [val+2] * numElements

        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList)
        head,tail  = linkedList.head(), linkedList.tail()

        linkedList.delete(val, all=True)

        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))
    
    def test_delete_head(self):
        val = 3
        N = 17
        
        regList  = [val]*N + [val+2]*2*N
        regList2  = [val+2]*2*N

        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList2)
        head,tail  = get_n_th_node(linkedList, N), linkedList.tail()

        linkedList.delete(val, all=True)

        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))

    def test_delete_tail(self):
        val = 3
        N = 17
        
        regList  =  [val+2]*2*N + [val]*N
        regList2  = [val+2]*2*N

        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList2)
        head,tail  = linkedList.head(), get_n_th_node(linkedList, 2*N-1)

        linkedList.delete(val, all=True)

        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))
    
    def test_delete_head_tail_and_middle(self):
        val = 3
        N = 17
        
        regList  =  [val]*N + [val+2]*N + [val]*2 + [val+2]*N + [val]*N
        regList2  = [val+2]*2*N

        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList2)
        head,tail  = get_n_th_node(linkedList, N), get_n_th_node(linkedList, 3*N+2-1)

        linkedList.delete(val, all=True)

        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))

    def test_delete_all(self):
        val = 3
        N = 17
        regList = [val]*N
        linkedList = make_linked_list(regList)
        expectedLinkedList = LinkedList2()
        
        head,tail  = linkedList.dummyTail, linkedList.dummyHead        
        linkedList.delete(val, all=True)

        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))


class TestInsert(unittest.TestCase):
    
    def test_insert_to_list(self):
        val = 3
        N = 17
        insertPos = N - 4

        regList  =  [val]*N
        regList2  = [val]*insertPos + [val+1] + [val]*(N-insertPos)

        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList2)
        head,tail  = linkedList.head(), linkedList.tail()

        node = Node(val+1)
        linkedList.insert(get_n_th_node(linkedList, insertPos-1), node)
        
        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual(node, get_n_th_node(linkedList, insertPos))
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))

    def test_insert_into_one_elem_list(self):
        val = 3
        regList  = [val+1]
        regList2 = [val+1] + [val]
        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList2)

        node = Node(val)
        head,tail  = linkedList.head(), node

        linkedList.insert(linkedList.head(), node)
        
        self.assertEqual(linkedList, expectedLinkedList)        
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))        

    def test_insert_into_one_elem_list_tail(self):
        val = 3
        regList  = [val+1]
        regList2 = [val+1] + [val]
        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList2)

        node = Node(val)
        head,tail  = linkedList.head(), node

        linkedList.insert(None, node)
        
        self.assertEqual(linkedList, expectedLinkedList)        
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))       
    
    def test_insert_to_empty(self):
        val = 3
        regList  = [val]

        linkedList = LinkedList2()
        expectedLinkedList = make_linked_list(regList)

        node = Node(val)
        head,tail  = node, node
        linkedList.insert(None, node)
        
        self.assertEqual(linkedList, expectedLinkedList)        
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))

    def test_insert_into_tail(self):
        val = 3
        N = 17
        insertPos = N

        regList  = [val+1]*N
        regList2 = [val+1]*N + [val]

        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList2)

        node = Node(val)
        head,tail  = linkedList.head(), node

        linkedList.insert(None, node)
        
        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual(node, get_n_th_node(linkedList, N))
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))

    def test_insert_after_head(self):
        val = 3
        N = 17  
        insertPos = N

        regList  = [val+1]*N
        regList2 = [val+1]+[val]+[val+1]*(N-1)

        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList2)

        head,tail  = linkedList.head(), linkedList.tail()

        node = Node(val)
        linkedList.insert(linkedList.head(), node)
        
        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual(node, get_n_th_node(linkedList, 1))
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))

class TestAddInHead(unittest.TestCase):

    def test_add_in_empty_list(self):
        val = 3
        N = 17  

        regList  = [val]

        linkedList = LinkedList2()
        expectedLinkedList = make_linked_list(regList)

        node = Node(val)
        linkedList.add_in_head(node)
        head,tail = node,node
        
        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual(node, get_n_th_node(linkedList, 0))        
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))

    def test_add_in_head(self):
        val = 3
        N = 17  

        regList  = [val+1]*N
        regList2 = [val]+[val+1]*N

        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList2)

        node = Node(val)
        linkedList.add_in_head(node)

        head,tail = node,linkedList.tail()
        
        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual(linkedList.head().next, get_n_th_node(linkedList, 1))
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))

    def test_add_in_head_one_elem_list(self):
        val = 3          

        regList  = [val+1]
        regList2 = [val]+[val+1]

        linkedList = make_linked_list(regList)
        expectedLinkedList = make_linked_list(regList2)

        node = Node(val)
        linkedList.add_in_head(node)

        head,tail = node,linkedList.tail()
        
        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual(linkedList.head().next, get_n_th_node(linkedList, 1))
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))

class TestClean(unittest.TestCase):

    def test_clean(self):
        val = 3
        N = 17  

        regList  = [val]*N        
        linkedList = make_linked_list(regList)
        expectedLinkedList = LinkedList2()
        head,tail = linkedList.dummyTail, linkedList.dummyHead
        
        linkedList.clean()
        
        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))

    def test_clean_empty(self):
        linkedList = LinkedList2()
        expectedLinkedList = LinkedList2()
        head,tail = linkedList.dummyTail, linkedList.dummyHead
        
        linkedList.clean()
        
        self.assertEqual(linkedList, expectedLinkedList)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))

class TestLen(unittest.TestCase):

    def test_len_empty(self):
        expectedLen = 0
        linkedList = LinkedList2()
        head,tail = linkedList.dummyTail, linkedList.dummyHead
        
        self.assertEqual(linkedList.len(), expectedLen)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))

    def test_len(self):
        expectedLen = 34
        val = 5
        regList = [val]*expectedLen
        linkedList = make_linked_list(regList)
        head,tail = linkedList.head(),linkedList.tail()
        
        self.assertEqual(linkedList.len(), expectedLen)
        self.assertEqual((head, tail), (linkedList.head(), linkedList.tail()))
        