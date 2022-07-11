
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def __eq__(self, other):
        selfNodeFwd, otherNodeFwd = self.head, other.head
        selfNodeBack, otherNodeBack = self.tail, other.tail

        result = True
        
        while True:
            if (selfNodeFwd, otherNodeFwd) == (None, None) and (selfNodeBack, otherNodeBack) == (None, None):
                return True

            if selfNodeFwd == None or otherNodeFwd == None:
                return False

            if selfNodeBack == None or otherNodeBack == None:
                return False
            
            if selfNodeFwd.value != otherNodeFwd.value:
                return False

            if selfNodeBack.value != otherNodeBack.value:
                return False
            
            selfNodeFwd, otherNodeFwd   = selfNodeFwd.next, otherNodeFwd.next
            selfNodeBack, otherNodeBack = selfNodeBack.prev, otherNodeBack.prev


    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next

        return None

    def find_all(self, val):
        node = self.head
        result = []
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def delete(self, val, all=False):
        node = self.head

        while node is not None:
            if node.value == val:
                prev = node.prev
                next = node.next

                if prev is not None: 
                    prev.next = next
                else:
                    self.head = next
                
                if next is not None:
                    next.prev = prev
                else:  
                    self.tail = prev 

                if not all:
                    return

            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length 

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
                return 
            else:
                prevTail = self.tail
                self.tail = newNode
                newNode.prev = prevTail
                newNode.next = None
                prevTail.next = newNode
                return
        else:
            next = afterNode.next 
            afterNode.next = newNode

        next.prev = newNode
        newNode.next = next
        newNode.prev = afterNode
        

    def add_in_head(self, newNode):
        prevHead = self.head
        self.head = newNode
        self.head.prev = None

        if prevHead is not None:
            prevHead.prev  = self.head
            self.head.next = prevHead
        else:
            self.tail = newNode
            
     
            