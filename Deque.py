class Deque:
    def __init__(self):
        self.container = []

    def addFront(self, item):
        self.container.insert(0, item)

    def addTail(self, item):
        self.container.append(item)

    def removeFront(self):
        if self.size() == 0:
            return None
        val = self.container[0]
        del self.container[0]
        return val

    def removeTail(self):
        if self.size() == 0:            
            return None        
        return self.container.pop()

    def size(self):
        return len(self.container)