from LinkedList import Node, LinkedList

def SumLinkedLists(list1, list2):
    sumList = LinkedList()
    
    if list1.len() != list2.len():
       return sumList
    
    node1 = list1.head
    node2 = list2.head
    prevSumNode  = None
    
    while node1 is not None and node2 is not None:
        sumNode = Node(node1.value + node2.value)
        sumList.insert(prevSumNode, sumNode)
        
        prevSumNode = sumNode        
        node1 = node1.next
        node2 = node2.next
    
    return sumList