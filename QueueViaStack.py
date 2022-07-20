from Stack import Stack

class Queue:
    def __init__(self):
        self.deqStack = Stack()
        self.enqStack = Stack()
    
    def _rearrange(self):
        while self.enqStack.size() > 0:            
            self.deqStack.push(self.enqStack.pop())
    
    def enqueue(self, item):
        self.enqStack.push(item)

    def dequeue(self):
        if self.deqStack.size() == 0:
            self._rearrange()
        return self.deqStack.pop()

    def size(self):
        return self.deqStack.size() + self.enqStack.size()