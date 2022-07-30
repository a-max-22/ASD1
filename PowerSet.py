# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet:

    def __init__(self):
        self.container = dict()

    def size(self):
        return len(self.container)

    def put(self, value):
        self.container[value] = 0

    def get(self, value):       
        return value in self.container

    def remove(self, value):
        if value in self.container:
            del self.container[value]
            return True
        return False

    def intersection(self, set2):
        intersection = PowerSet()
        for e in self.container:
            if not set2.get(e): continue
            intersection.put(e)
        return intersection 

    def union(self, set2):
        union = PowerSet()        
        for e in self.container:
            union.put(e)  
        for e in set2.container:
            union.put(e)
        return union

    def difference(self, set2):
        diff = PowerSet()
        for e in self.container:
            if set2.get(e): continue
            diff.put(e)        
        return diff

    def issubset(self, set2):
        for e in self.container:
            if not set2.get(e): 
                return False                
        return True