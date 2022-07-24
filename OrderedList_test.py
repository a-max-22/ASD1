import unittest

from OrderedList import OrderedList, OrderedStringList, Node


def make_ordered_list(lst, asc):
    ordLst = OrderedList(asc)
    for item in lst:
        ordLst.add(item)
    return ordLst

def checkNodesValues(nodes,values):    
    for (node,value) in zip(nodes,values):
        if node.value != value:
            return False            
    return len(nodes) == len(values)

def checkNodesLinks(nodes):
    if len(nodes) == 0:
        return True
    nodesChecked = 0
    
    nextNode = nodes[0].next
    for node in nodes:
        if nextNode is not None and nextNode.prev != node:
            return False
        if nextNode is None and nodesChecked < len(nodes)-1:
            return False
        if node.next != nextNode:
            return False
        node = node.next 
        nextNode = nextNode.next if nextNode is not None else None
        nodesChecked += 1    
    return True

def checkNodesValuesOrdered(nodes, asc):
    prev = nodes[0].value
    for node in nodes:
        if prev > node.value and asc:
            return False
        if prev < node.value and not asc:
            return False
    return True

class TestCompare(unittest.TestCase):

    def test_equals(self):
        lst = OrderedList(asc = True)        
        self.assertEqual(lst.compare(3,3), 0)
        
    def test_less_than(self):
        lst = OrderedList(asc = True)        
        self.assertEqual(lst.compare(1,3), -1)
        
    def test_more_than(self):
        lst = OrderedList(asc = True)
        self.assertEqual(lst.compare(3,1), 1)


class TestAdd(unittest.TestCase):
    
    def test_add_to_empty_asc(self):
        val = 12
        lst = OrderedList(asc = True)
        lst.add(val)
        contents = lst.get_all()
        self.assertTrue(checkNodesValues(contents, [val]))
        self.assertTrue(checkNodesLinks(contents))
        self.assertEqual((lst.head, lst.tail),(contents[0],contents[0]))
        
    def test_add_to_single_elem_list_tail_asc(self):
        val = 12
        lst = OrderedList(asc = True)
        lst.add(val)
        lst.add(val+1)
        contents = lst.get_all()
        self.assertTrue(checkNodesValues(contents, [val, val+1]))
        self.assertTrue(checkNodesLinks(contents))
        self.assertEqual((lst.head, lst.tail),(contents[0],contents[1]))

    def test_add_to_single_elem_list_tail_desc(self):
        val = 12
        lst = OrderedList(asc = False)
        lst.add(val)
        lst.add(val+1)
        contents = lst.get_all()
        self.assertTrue(checkNodesValues(contents, [val+1, val]))
        self.assertTrue(checkNodesLinks(contents))
        self.assertEqual((lst.head, lst.tail),(contents[0],contents[1]))
        
    def test_add_to_single_elem_list_head_asc(self):
        val = 12
        lst = OrderedList(asc = True)
        lst.add(val)
        lst.add(val-1)
        contents = lst.get_all()
        self.assertTrue(checkNodesValues(contents, [val-1, val]))
        self.assertTrue(checkNodesLinks(contents))
        self.assertEqual((lst.head, lst.tail),(contents[0],contents[-1]))

    def test_add_to_single_elem_list_head_desc(self):
        val = 12
        lst = OrderedList(asc = False)
        lst.add(val)
        lst.add(val-1)
        contents = lst.get_all()
        self.assertTrue(checkNodesValues(contents, [val,val-1]))
        self.assertTrue(checkNodesLinks(contents))
        self.assertEqual((lst.head, lst.tail),(contents[0],contents[-1]))
        
    def test_add_to_multi_elem_list_asc(self):
        N = 13
        actual = [x for x in range(N)] + [N+1]
        expected = [x for x in range(N+2)]
        lst = make_ordered_list(actual, asc = True)
        actualNodes = lst.get_all()        
        lst.add(N)
        contents = lst.get_all()
        self.assertTrue(checkNodesValues(contents, expected))
        self.assertTrue(checkNodesLinks(contents))
        self.assertEqual((lst.head, lst.tail),(actualNodes[0], actualNodes[-1]))

    def test_add_to_multi_elem_list_desc(self):
        N = 13
        actual = [x for x in range(N)] + [N+1]
        expected = [x for x in range(N+1,-1,-1)]
        lst = make_ordered_list(actual, asc = False)
        actualNodes = lst.get_all()
        lst.add(N)
        contents = lst.get_all()
        self.assertTrue(checkNodesValues(contents, expected))
        self.assertTrue(checkNodesLinks(contents))
        self.assertEqual((lst.head, lst.tail),(actualNodes[0], actualNodes[-1]))
    
    def test_add_to_head_multi_asc(self):
        N = 13
        actual = [x for x in range(1,N)]
        expected = [x for x in range(N)]
        lst = make_ordered_list(actual, asc = True)
        actualNodes = lst.get_all()        
        lst.add(0)
        contents = lst.get_all()
        self.assertTrue(checkNodesValues(contents, expected))
        self.assertTrue(checkNodesLinks(contents))

    def test_add_to_head_multi_desc(self):
        N = 13
        actual = [x for x in range(N)]
        expected = [x for x in range(N,-1,-1)]
        lst = make_ordered_list(actual, asc = False)
        actualNodes = lst.get_all()        
        lst.add(N)
        contents = lst.get_all()
        self.assertTrue(checkNodesValues(contents, expected))
        self.assertTrue(checkNodesLinks(contents))
        
    def test_add_to_tail_multi_asc(self):
        N = 13
        actual = [x for x in range(N)]
        expected = [x for x in range(N+1)]
        lst = make_ordered_list(actual, asc = True)
        actualNodes = lst.get_all()        
        lst.add(N)
        contents = lst.get_all()
        self.assertTrue(checkNodesValues(contents, expected))
        self.assertTrue(checkNodesLinks(contents))

    def test_add_to_tail_multi_desc(self):
        N = 13
        actual = [x for x in range(1,N)]
        expected = [x for x in range(N-1,-1,-1)]
        lst = make_ordered_list(actual, asc = False)
        actualNodes = lst.get_all()        
        lst.add(0)
        contents = lst.get_all()
        self.assertTrue(checkNodesValues(contents, expected))
        self.assertTrue(checkNodesLinks(contents))


class TestFind(unittest.TestCase):
    
    def test_find_empty_asc(self):
        val = 12
        lst = OrderedList(asc = True)
        node = lst.find(val)
        contents = lst.get_all()
        self.assertTrue(node is None)
        self.assertTrue(checkNodesValues(contents, []))
        self.assertTrue(checkNodesLinks(contents))
        self.assertEqual((lst.head, lst.tail),(None, None))

    def test_find_absent_single_asc(self):
        val = 3
        actual = [val+1]
        lst = make_ordered_list(actual, asc = True)
        node = lst.find(val)
        contents = lst.get_all()
        self.assertTrue(node is None)
        self.assertTrue(checkNodesValues(contents, actual))
        self.assertTrue(checkNodesLinks(contents))
    
    def test_find_absent_multi_asc(self):
        val = 3
        actual = [x for x in range(1,val)] + [x for x in range(val+1,val+3)]
        lst = make_ordered_list(actual, asc = True)
        node = lst.find(val)
        contents = lst.get_all()
        self.assertTrue(node is None)
        self.assertTrue(checkNodesValues(contents, actual))
        self.assertTrue(checkNodesLinks(contents))

    def test_find_absent_multi_desc(self):
        val = 3
        actual = [x for x in range(1,val)] + [x for x in range(val+1,val+3)]
        lst = make_ordered_list(actual, asc = False)
        node = lst.find(val)
        contents = lst.get_all()
        self.assertTrue(node is None)
        self.assertTrue(checkNodesValues(contents, actual[::-1]))
        self.assertTrue(checkNodesLinks(contents))
    
    def test_find_in_the_middle_asc(self):
        val = 3
        actual = [x for x in range(0,val+3)]
        lst = make_ordered_list(actual, asc = True)
        node = lst.find(val)
        contents = lst.get_all()
        self.assertEqual(node, contents[val])
        self.assertTrue(checkNodesValues(contents, actual))
        self.assertTrue(checkNodesLinks(contents))

    def test_find_in_head(self):
        val = 0
        actual = [x for x in range(0,val+3)]
        lst = make_ordered_list(actual, asc = True)
        node = lst.find(val)
        contents = lst.get_all()
        self.assertEqual(node, contents[val])
        self.assertTrue(checkNodesValues(contents, actual))
        self.assertTrue(checkNodesLinks(contents))

    def test_find_in_tail(self):
        val = 14
        actual = [x for x in range(0,val)]
        lst = make_ordered_list(actual, asc = True)
        node = lst.find(val-1)      
        contents = lst.get_all()
        self.assertEqual(node, contents[val-1])
        self.assertTrue(checkNodesValues(contents, actual))
        self.assertTrue(checkNodesLinks(contents))

    def test_find_in_one_elem_list(self):
        val = 14
        actual = [val]
        lst = make_ordered_list(actual, asc = True)
        node = lst.find(val)
        contents = lst.get_all()
        self.assertEqual(node, contents[0])
        self.assertTrue(checkNodesValues(contents, actual))
        self.assertTrue(checkNodesLinks(contents))

    def test_find_among_multiple_equal_elems(self):
        N = 7
        actual = [x for x in range(N)] + [N]*3 + [x for x in range(N+1,N+4)]
        lst = make_ordered_list(actual, asc = True)
        node = lst.find(N)
        contents = lst.get_all()        
        self.assertEqual(node, contents[N+3-1])
        self.assertTrue(checkNodesValues(contents, actual))
        self.assertTrue(checkNodesLinks(contents))

class TestDelete(unittest.TestCase):
    
    def test_del_empty(self):
        val = 12
        lst = OrderedList(asc = True)
        node = lst.delete(val)
        contents = lst.get_all()
        self.assertTrue(node is None)
        self.assertTrue(checkNodesValues(contents, []))
        self.assertTrue(checkNodesLinks(contents))
        self.assertEqual((lst.head, lst.tail),(None, None))

    def test_del_absent(self):
        val = 3
        actual = [x for x in range(1,val)] + [x for x in range(val+1,val+3)]
        lst = make_ordered_list(actual, asc = True)
        node = lst.delete(val)
        contents = lst.get_all()
        self.assertTrue(node is None)
        self.assertTrue(checkNodesValues(contents, actual))
        self.assertTrue(checkNodesLinks(contents))
    
    def test_del_in_the_middle(self):
        val = 3
        C = 4
        actual = [x for x in range(0,val)] + [val]*C + [x for x in range(val+1,val+3)]
        expected = [x for x in range(0,val)] + [val]*(C-1)+ [x for x in range(val+1,val+3)]        
        lstAsc = make_ordered_list(actual, asc = True)
        lstAsc.delete(val)
        contents = lstAsc.get_all()
        self.assertTrue(checkNodesValues(contents, expected))
        self.assertTrue(checkNodesLinks(contents))
        
        lstDesc = make_ordered_list(actual, asc = False)
        lstDesc.delete(val)
        contents = lstDesc.get_all()
        self.assertTrue(checkNodesValues(contents, expected[::-1]))
        self.assertTrue(checkNodesLinks(contents))

    def test_del_head(self):
        N = 17
        C = 1
        actual = [0]*C + [x for x in range(1,N)]        
        lst = make_ordered_list(actual, asc = True)
        before = lst.get_all()
        lst.delete(0)
        after = lst.get_all()
        self.assertTrue(checkNodesValues(after, actual[C:]))
        self.assertTrue(checkNodesLinks(after))
        self.assertEqual((lst.head, lst.tail), (before[C], before[-1]))
        
    def test_del_tail(self):
        N = 17
        C = 1
        actual = [x for x in range(0,N)] + [N]*C
        lst = make_ordered_list(actual, asc = True)
        before = lst.get_all()
        lst.delete(N)
        after = lst.get_all()
        self.assertTrue(checkNodesValues(after, actual[:N]))
        self.assertTrue(checkNodesLinks(after))
        self.assertEqual((lst.head, lst.tail), (before[0], before[-C-1]))
        
    def test_del_single(self):
        N = 17        
        actual = [N]
        lst = make_ordered_list(actual, asc = True)
        before = lst.get_all()
        lst.delete(N)
        after = lst.get_all()
        self.assertTrue(checkNodesValues(after, []))        
        self.assertEqual((lst.head, lst.tail), (None, None))
        
class TestClean(unittest.TestCase):

    def test_clean_empty(self):
        lst = OrderedList(asc = True)
        node = lst.clean(asc = True)
        contents = lst.get_all()
        self.assertTrue(node is None)
        self.assertTrue(checkNodesValues(contents, []))
        self.assertTrue(checkNodesLinks(contents))
        self.assertEqual((lst.head, lst.tail),(None, None))

    def test_clean_non_empty(self):
        lst = make_ordered_list([0]*12, asc = True)
        node = lst.clean(asc = True)
        contents = lst.get_all()
        self.assertTrue(node is None)
        self.assertTrue(checkNodesValues(contents, []))
        self.assertTrue(checkNodesLinks(contents))
        self.assertEqual((lst.head, lst.tail),(None, None))

class TestLen(unittest.TestCase):
    
    def test_len_empty(self):
        lst = OrderedList(asc = True)
        contents = lst.get_all()
        self.assertTrue(checkNodesValues(contents, []))
        self.assertTrue(checkNodesLinks(contents))
        self.assertEqual((lst.head, lst.tail),(None, None))
        self.assertEqual(lst.len(),0 )
    
    def test_len_non_empty(self):
        N = 13
        lst = make_ordered_list([0]*N, asc = True)
        contents = lst.get_all()
        self.assertTrue(checkNodesValues(contents, [0]*N))
        self.assertTrue(checkNodesLinks(contents))
        self.assertEqual((lst.head, lst.tail),(contents[0], contents[-1]))
        self.assertEqual(lst.len(),N)

class TestOrderedStringList(unittest.TestCase):
    
    def test_equals(self):
        lst = OrderedStringList(asc = True)        
        self.assertEqual(lst.compare('a','a'), 0)
        self.assertEqual(lst.compare('  a ','           a     '), 0)

    def test_less_than(self):
        lst = OrderedStringList(asc = True)        
        self.assertEqual(lst.compare('a','c'), -1)
        self.assertEqual(lst.compare('a','aa'), -1)
        self.assertEqual(lst.compare('aa','ab'), -1)
        self.assertEqual(lst.compare('     aa  ','      ab     '), -1)

    def test_more_than(self):
        lst = OrderedStringList(asc = True)        
        self.assertEqual(lst.compare('c','a'), 1)
        self.assertEqual(lst.compare('aa','a'), 1)
        self.assertEqual(lst.compare('ab','aa'), 1)
        self.assertEqual(lst.compare('        ab  ','      aa    '), 1)
        