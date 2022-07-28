class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.step = 1

    def hash_fun(self, key):
        hash = 0
        for s in key:
            hash = (hash + ord(s)) % self.size
        return hash

    def is_key(self, key):
        slot = self.find(key)
        if slot is None:
            return False
        return True
    
    def __seek_slot(self, key):
        slot = None        
        slot = self.hash_fun(key)
        initialSlot = slot
        while self.slots[slot] is not None:
            if self.slots[slot] == key:
                return slot
            slot = (slot + self.step) % self.size
            if slot == initialSlot:
                return None      
        return slot
    
    def put(self, key, value):
        slot = self.__seek_slot(key)
        if slot == None:
            raise KeyError("No free slot for key")
        self.slots[slot] = key
        self.values[slot] = value

    def find(self, key):
        slot = self.hash_fun(key)
        initialSlot = slot
        while self.slots[slot] is not None:
            if self.slots[slot] == key:
                return slot
            slot = (slot + self.step) % self.size
            if slot == initialSlot:
                return None
        return None   
        
    def get(self, key):
        slot = self.find(key)
        if slot is None:
            return None            
        return self.values[slot]