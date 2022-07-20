class Queue:
    def __init__(self):
        self.container = []        

    def enqueue(self, item):
        self.container.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None            
        result = self.container[0]
        del self.container[0]
        return result

    def size(self):
        return len(self.container)