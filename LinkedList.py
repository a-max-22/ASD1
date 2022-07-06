class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        
    def __eq__(self, other):
        selfNode  = self.head
        otherNode = other.head
        result = True
        
        while True:
            if (selfNode, otherNode) == (None, None):
                return True
                
            if selfNode == None or otherNode == None:
                return False
            
            if selfNode.value != otherNode.value:
                return False
            
            selfNode = selfNode.next
            otherNode = otherNode.next                        
                
    
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        nodes = []
        node  = self.head
        while not node is None:
            if node.value == val:
                nodes.append(node)
            
            node = node.next            
            
        return nodes

    def delete(self, val, all=False):
        node = self.head
        prev = Node(None)
        prev.next = self.head
        
        while not node is None:
            if node.value == val:                
                if prev.value is None:
                    self.head = node.next
                    prev.next = self.head
                else:
                    prev.next = node.next            
                
                if node.next is None:
                    self.tail = None if prev.value is None else prev
                    
                if not all:
                    return
            else:        
                prev = prev.next
                
            node = node.next

            
    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        listLen = 0
        node = self.head
        while node is not None:
            listLen += 1
            node = node.next
            
        return listLen

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            return
        
        if afterNode.next is None:
            self.tail = newNode
        
        newNode.next = afterNode.next
        afterNode.next = newNode