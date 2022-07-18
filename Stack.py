
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
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)        

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[-1]