class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 == v2: 
            return 0
        return -1 if v1 < v2 else 1
        
    def add(self, value):
        newNode = Node(value)
        nextNode = self.find_next_node_by_order(value)
        if nextNode is None and self.tail is not None:
            prevTail = self.tail
            prevTail.next = newNode
            newNode.prev = prevTail
            self.tail = newNode
            return            
        if nextNode is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
            return
        if nextNode == self.head:
            self.head = newNode
        if nextNode.prev is not None:
            nextNode.prev.next = newNode
        newNode.next = nextNode
        newNode.prev = nextNode.prev
        nextNode.prev = newNode
        
    def find_next_node_by_order(self, value):
        node = self.head
        while node is not None:
            if self.__ascending and self.compare(node.value, value) == 1:
                return node
            if not self.__ascending and self.compare(node.value, value) == -1:
                return node
            node = node.next
        return None
        
    def find(self, val):
        if self.tail is None:
            return None
        nextNode = self.find_next_node_by_order(val)
        if nextNode is None:
            return self.tail if self.tail.value == val else None
        if nextNode.prev.value != val:
            return None
        return nextNode.prev

    def delete(self, val):
        if self.head is None:
            return
        nextNode = self.find_next_node_by_order(val)
        prevNode = nextNode.prev if nextNode is not None else self.tail
        while prevNode is not None:
            if prevNode.value != val:
                break
            prevNode = prevNode.prev
        if nextNode is None:
            self.tail = prevNode
        if nextNode is not None:
            nextNode.prev = prevNode
        if prevNode is None:
            self.head = nextNode
            return
        prevNode.next = nextNode
        
    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, s1, s2):
        v1 = s1.strip()
        v2 = s2.strip()        
        if v1 == v2: 
            return 0
        return -1 if v1 < v2 else 1
        