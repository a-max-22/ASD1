from LinkedList import *

def make_linked_list(initialList):        
    result = LinkedList()
    for val in initialList:
        result.add_in_tail(Node(val))
            
    return result

def get_linked_list_second_to_last_node(linkedList):
    node = linkedList.head
    prev = None
    while node is not None:
        prev = node
        node = node.next
    
    return prev

def get_n_th_node(linkedList, n):
    node = linkedList.head
    prev = None
    i = 0
    
    while node is not None and i < n:
        i += 1
        node = node.next
        
    return node
    

class TestEquality:

    def test_empty_equals_empty(self):
        emptyList1 = LinkedList()
        emptyList2 = LinkedList()
        assert  emptyList1 == emptyList2
    
    def test_empty_neq_non_empty(self):
        emptyList = LinkedList()
        nonEmptyList = make_linked_list([1,2,3])
        singleElemList = make_linked_list([1])
        assert  not (emptyList == nonEmptyList)
        assert  not (emptyList == singleElemList)
    
    def test_eq_size_one(self):
        list1 = make_linked_list([1])
        list2 = make_linked_list([1])
        assert  list1 == list2

    def test_neq_size_one(self):
        list1 = make_linked_list([1])
        list2 = make_linked_list([2])
        assert  list1 != list2
    
    def test_eq_size_n(self):
        list1 = make_linked_list([1,2,3,4,5,6,7,8,9,10,11,12])
        list2 = make_linked_list([1,2,3,4,5,6,7,8,9,10,11,12])
        list3 = make_linked_list([1,2,3,4,5,6,7,8,9,10,11,0])
        list4 = make_linked_list([0,2,3,4,5,6,7,8,9,10,11,12])
        assert  list1 == list2
        assert  list1 != list3
        assert  list1 != list4
    
    def test_diff_size_lists(self):
        list1 = make_linked_list([1,2,3,4,5,6,7,8,9,10,11,12])
        list2 = make_linked_list([1,2,3,4,5,6,7,8])
        list3 = make_linked_list([8,9,10,11,12])
        assert  list1 != list2
        assert  list2 != list3


class TestDeleteOne:

    def test_deletion(self):
        valueToDelete = 8
        
        list1 = make_linked_list([1,2,3,4,5,6,7,8,9])
        list2 = make_linked_list([1,2,3,4,5,6,7,9])
        
        (head, tail) = (list1.head, list1.tail) 
        list1.delete(valueToDelete, all=False)
        
        assert list1 == list2
        assert (head,tail) == (list1.head, list1.tail)

    def test_if_deletes_first_val(self):
        valueToDelete = 3
        
        list1 = make_linked_list([1,2,3,3,3,3,7,8,9])
        list2 = make_linked_list([1,2,3,3,3,7,8,9])
        
        (head, tail) = (list1.head, list1.tail)
        list1.delete(valueToDelete, all=False)
        
        assert list1 == list2
        assert (head,tail) == (list1.head, list1.tail)
        

        
    def test_not_delete_if_none(self):
        valueToDelete = 0
        list1 = make_linked_list([1,2,3,4,5,6,7,8,9])
        list2 = make_linked_list([1,2,3,4,5,6,7,8,9])
        
        (head, tail) = (list1.head, list1.tail)
        list1.delete(valueToDelete, all=False)
        
        assert list1 == list2 
        assert (head,tail) == (list1.head, list1.tail)


    def test_delete_first_val(self):
        valueToDelete = 1
        list1 = make_linked_list([1,2,3,4])
        list2 = make_linked_list([2,3,4])
        
        (head, tail) = (list1.head.next, list1.tail) 
        list1.delete(valueToDelete, all=False)

        assert list1 == list2
        assert (head,tail) == (list1.head, list1.tail)

    
    def test_delete_last_val(self):
        valueToDelete = 4
        list1 = make_linked_list([1,2,3,4])
        list2 = make_linked_list([1,2,3])
        list1.delete(valueToDelete, all=False)
        
        (head, tail) = (list1.head, get_linked_list_second_to_last_node(list1))
        
        assert list1 == list2
        assert (head,tail) == (list1.head, list1.tail)
    
    def test_delete_last_val_for_empty(self):
        valueToDelete = 4
        list1 = make_linked_list([4])
        list2 = LinkedList()
        
        (head, tail) = (None, None)
        list1.delete(valueToDelete, all=False)
        
        assert list1 == list2
        assert (head,tail) == (list1.head, list1.tail)


    
class TestDeleteMultiple:
    
    def test_deletion(self):
        valueToDelete = 4
        
        list1 = make_linked_list([1,2,4,4,5,6,4,4,9])
        list2 = make_linked_list([1,2,5,6,9])
        
        (head, tail) = (list1.head, list1.tail) 
        list1.delete(valueToDelete, all=True)
        
        assert list1 == list2
        assert (head,tail) == (list1.head, list1.tail)

    def test_delete_first_val(self):
        val = 1
        
        list1 = make_linked_list([val,val,val+2,val+3,val,val,val+4,val+5])
        list2 = make_linked_list([val+2,val+3,val+4,val+5])
        
        (head, tail) = (list1.head.next.next, list1.tail) 
        list1.delete(val, all=True)        
        
        assert list1 == list2
        assert (head,tail) == (list1.head, list1.tail)
    
    def test_delete_last_val(self):
        val = 1
        regularList = [val,val,val+2,val,val,val+5,val,val]
        
        list1 = make_linked_list(regularList)
        list2 = make_linked_list([val+2,val+5])
        
        (head, tail) = (list1.head.next.next, get_n_th_node(list1, len(regularList)-3)) 
        list1.delete(val, all=True)                
        
        assert list1 == list2
        assert (head,tail) == (list1.head, list1.tail)
    
    def test_delete_all(self):
        valueToDelete = 1
        regularList = [valueToDelete]*10        
        
        list1 = make_linked_list(regularList)
        list2 = LinkedList()
        
        (head, tail) = (None, None) 
        list1.delete(valueToDelete, all=True)
        
        assert list1 == list2
        assert (head,tail) == (list1.head, list1.tail)


class TestClear:
    
    def test_clear_non_empty(self):
        regularList = [1,1,1,1,1,1]
        list1 = make_linked_list(regularList)

        list1 = make_linked_list(regularList)
        list2 = LinkedList()
        
        (head, tail) = (None, None) 
        list1.clean()
        
        assert list1 == list2
        assert (head,tail) == (list1.head, list1.tail)
    
    def test_clear_empty(self):        
        list1 = LinkedList()
        list2 = LinkedList()
        
        (head, tail) = (None, None) 
        list1.clean()
        
        assert list1 == list2
        assert (head,tail) == (list1.head, list1.tail)


class TestFindAll:
    def test_find_single(self):
        val = 1
        regularList = [val+3,val+1,val+2,val,val+5]
        
        list1 = make_linked_list(regularList)
        list2 = make_linked_list([val+2,val+5])
        
        (head, tail) = (list1.head, list1.tail) 
        result = list1.find_all(val)                
        
        assert result == [get_n_th_node(list1, 3)]
        assert (head,tail) == (list1.head, list1.tail)

    
    def test_find_multiple(self):
        val = 1
        regularList = [val, val+3, val, val+1,val+2,val,val+5, val, val]
        
        list1 = make_linked_list(regularList)
        
        (head, tail) = (list1.head, list1.tail) 
        result = list1.find_all(val)                
        
        assert result == [get_n_th_node(list1, 0), get_n_th_node(list1, 2), get_n_th_node(list1, 5), get_n_th_node(list1, 7), get_n_th_node(list1, 8)]
        
        assert (head,tail) == (list1.head, list1.tail)

        
    def test_find_absent_node(self):
        val = 1
        regularList = [val+3, val+1,val+2,val+5]
        
        list1 = make_linked_list(regularList)
        
        (head, tail) = (list1.head, list1.tail) 
        result = list1.find_all(val)                
        
        assert result == []        
        assert (head,tail) == (list1.head, list1.tail)

    
    def test_find_in_empty_list(self):                
        val   = 1
        list1 = LinkedList()
        
        (head, tail) = (None, None) 
        result = list1.find_all(val)                
        
        assert result == []        
        assert (head,tail) == (list1.head, list1.tail)
    
class TestLen:
    
    def test_empty_len(self):
        val   = 1
        list1 = LinkedList()
        
        (head, tail) = (None, None) 
        result = list1.len()                
        
        assert result == 0        
        assert (head,tail) == (list1.head, list1.tail)

    
    def test_single_elem_len(self):
        list1 = make_linked_list([1])
        
        (head, tail) = (list1.head, list1.tail)
        result = list1.len()                
        
        assert result == 1     
        assert (head,tail) == (list1.head, list1.tail)
    
    def test_mult_elem_len(self):
        length = 100
        list1  = make_linked_list([1]*length)
        
        (head, tail) = (list1.head, list1.tail)
        result = list1.len()                
        
        assert result == length        
        assert (head,tail) == (list1.head, list1.tail)
    
    
class TestInsert:

    def test_insert(self):
        val = 1
        length = 20
        insertPos = 10
        regularList = [val]*length
        
        list1 = make_linked_list(regularList)
        list2 = make_linked_list([val]*(insertPos+1) + [val+1] + [val]*(length - insertPos - 1))
        (head, tail) = (list1.head, list1.tail) 
        node = Node(val + 1)
        
        list1.insert(get_n_th_node(list1, insertPos), node)                
        assert list1 == list2
    
    def test_insert_after_first(self):
        val = 1
        length = 20
        insertPos = 1
        regularList = [val]*length
        
        list1 = make_linked_list(regularList)
        list2 = make_linked_list([val]*(insertPos+1) + [val+1] + [val]*(length - insertPos - 1))
        (head, tail) = (list1.head, list1.tail) 
        node = Node(val + 1)
        
        list1.insert(get_n_th_node(list1, insertPos), node)                
        assert list1 == list2

    def test_insert_end(self):
        val = 1
        length = 20
        insertPos = length-1
        regularList = [val]*length
        
        list1 = make_linked_list(regularList)
        list2 = make_linked_list([val]*(insertPos+1) + [val+1] + [val]*(length - insertPos - 1))
        node = Node(val + 1)
        
        (head, tail) = (list1.head, node)
        list1.insert(get_n_th_node(list1, insertPos), node)
        
        assert list1 == list2
        assert (head, tail) == (list1.head, list1.tail)

    def test_insert_at_beginning(self):
        val = 1
        length = 20
        
        regularList = [val]*length
        
        list1 = make_linked_list(regularList)
        list2 = make_linked_list([val+1] + [val]*(length))
        node = Node(val + 1)
        
        (head, tail) = (node, list1.tail) 
        list1.insert(None, node)                
        
        assert list1 == list2
        assert (head, tail) == (list1.head, list1.tail)

    def test_insert_into_empty_list(self):
        val = 1        
                
        list1 = LinkedList()
        list2 = make_linked_list([val+1])
        node = Node(val + 1)
        
        (head, tail) = (node, node) 
        list1.insert(None, node)                
        
        assert list1 == list2
        assert (head, tail) == (list1.head, list1.tail)
