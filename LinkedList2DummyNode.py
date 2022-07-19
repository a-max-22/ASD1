
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class DummyNode(Node):
    def __init__(self, v):
        super().__init__(v)
        

class LinkedList2:
    def __init__(self):
        self.dummyHead = DummyNode(None)
        self.dummyTail = DummyNode(None)
        self.dummyHead.next = self.dummyTail
        self.dummyHead.prev = self.dummyTail
        self.dummyTail.next = self.dummyHead
        self.dummyTail.prev = self.dummyHead

    def head(self):
        return self.dummyHead.next

    def tail(self):
        return self.dummyTail.prev
        
    def is_past_end(self, node):
        return isinstance(node, DummyNode)
    
    def is_empty(self):
        return isinstance(self.head(), DummyNode)
    
    def add_in_tail(self, item):
        prevTail = self.tail()
        prevTail.next = item
        item.prev = prevTail
        item.next = self.dummyTail
        self.dummyTail.prev = item        

    def __eq__(self, other):                                            
        selfNode, otherNode = self.head(), other.head()
        while not self.is_past_end(selfNode) and not other.is_past_end(otherNode):
            if selfNode.value != otherNode.value:
                return False
            selfNode, otherNode = selfNode.next, otherNode.next

        selfNode, otherNode = self.tail(), other.tail()
        while not self.is_past_end(selfNode) and not other.is_past_end(otherNode):
            if selfNode.value != otherNode.value:
                return False
            selfNode, otherNode = selfNode.prev, otherNode.prev
        
        return self.is_empty() == other.is_empty()

    def find(self, val):        
        node = self.head()
        while not self.is_past_end(node):
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head()
        while not self.is_past_end(node):
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head()
        while not self.is_past_end(node):
            if node.value != val:
                node = node.next
                continue               
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
            if not all:
                return
            node = next

    def clean(self):
        self.dummyHead.next = self.dummyTail
        self.dummyHead.prev = self.dummyTail
        self.dummyTail.next = self.dummyHead
        self.dummyTail.prev = self.dummyHead

    def len(self):
        length = 0
        node = self.head()
        while not self.is_past_end(node):
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        node = afterNode
        if node is None:
            node = self.tail()     
        next = node.next
        node.next = newNode
        next.prev = newNode
        newNode.prev = node
        newNode.next = next
        
    def add_in_head(self, newNode):      
        prevHead = self.head()
        self.dummyHead.next = newNode
        prevHead.prev = newNode
        newNode.next = prevHead
        newNode.prev = self.dummyHead
        