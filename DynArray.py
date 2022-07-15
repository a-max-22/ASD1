import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def _advance_count(self):
        if (self.count + 1 < self.capacity):
            self.count += 1
            return                
        self.resize(2 * self.capacity)
        self.count += 1

    def insert(self, i, itm):
        if (i < 0 or i > self.count ):
            raise IndexError('Insert to invalid index')
        
        self._advance_count()
        lastIndex = self.count - 1
        
        for j in range(lastIndex, i, -1):            
            self.array[j] = self.array[j-1]            
        
        self.array[i] = itm        

    
    def _reduce_count(self):
        self.count -= 1        
        if (self.count >= (self.capacity // 2)):
            return
        
        new_capacity = int(self.capacity / 1.5)
        if new_capacity < 16:
            new_capacity = 16            
        self.resize(new_capacity)
        

    def delete(self, i):
        if (i < 0 or i >= self.count ):
            raise IndexError('Delete from invalid position')
        
        lastIndex = self.count - 1        
        if (i == lastIndex):
            self._reduce_count()
            return            
        
        for j in range(i, lastIndex):            
            self.array[j] = self.array[j+1]
            
        self._reduce_count()