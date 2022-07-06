from SumLinkedLists import SumLinkedLists
from LinkedList import LinkedList, Node

def make_linked_list(initialList):        
    result = LinkedList()
    for val in initialList:
        result.add_in_tail(Node(val))
            
    return result


def test_sum():
    length = 10
    regList1 = [x for x in range(1,length)]
    regList2 = [x+1  for x in range(1,length)]
    regSumList = [x + y for x,y in zip(regList1, regList2)]
    
    list1 = make_linked_list(regList1)
    list2 = make_linked_list(regList2)
    sumList = make_linked_list(regSumList)
    
    assert SumLinkedLists(list1, list2) == sumList


def test_sum_empty_lists():
    list1 = LinkedList()
    list2 = LinkedList()
        
    assert SumLinkedLists(list1, list2) == LinkedList()
    
def test_sum_empty_and_nonempty():
    length = 10
    regList1 = [x for x in range(1,length)]
    
    list1 = make_linked_list(regList1)
    list2 = LinkedList()    

    assert SumLinkedLists(list1, list2) == LinkedList()

def test_sum_different_sized_lists():
    length = 10
    regList1 = [x for x in range(1,length)]
    regList2 = [x+1  for x in range(1,length-2)]
    
    list1 = make_linked_list(regList1)
    list2 = make_linked_list(regList2)
    
    assert SumLinkedLists(list1, list2) == LinkedList()

def test_sum_one_elem_lists():
    regList1 = [1]
    regList2 = [2]
    sumRegList = [3]

    list1 = make_linked_list(regList1)
    list2 = make_linked_list(regList2)
    sumList = make_linked_list(sumRegList)    

    assert SumLinkedLists(list1, list2) == sumList

