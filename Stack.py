
class Stack:
    def __init__(self):
        self.stack = []

    def __eq__(self, other):
        return self.stack == other.stack
        
    def size(self):
        return len(self.stack)

    def pop(self):        
        if self.size() == 0:
            return None
        res = self.stack[0]
        del self.stack[0]
        return res

    def push(self, value):
        self.stack.insert(0, value)        

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[0]