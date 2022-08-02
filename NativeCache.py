class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
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
        if slot is None:
            slot = self.__seek_slot_with_min_hits(key)        
        self.slots[slot] = key
        self.values[slot] = value
        self.hits[slot] = 1
        
    def __seek_slot_with_min_hits(self, key):
        slot = None
        slot = self.hash_fun(key)
        initialSlot = slot
        hits = self.hits[slot]
        minHitsSlot = slot
        while True:
            slot = (slot + self.step) % self.size
            if self.hits[slot] < self.hits[minHitsSlot]:
                minHitsSlot = slot            
            if slot == initialSlot:
                return minHitsSlot
        return minHitsSlot

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
        self.hits[slot] += 1
        return self.values[slot]
    