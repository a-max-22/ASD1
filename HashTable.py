class HashTable:    
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        hash = 0
        for s in value:
            hash = (hash + ord(s)) % self.size
        return hash

    def seek_slot(self, value):
        slot = None        
        slot = self.hash_fun(value)
        initialSlot = slot
        while self.slots[slot] is not None:
            if self.slots[slot] == value:
                return slot
            slot = (slot + self.step) % self.size
            if slot == initialSlot:
                return None      
        return slot

    def put(self, value):
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
        return slot

    def find(self, value):
        slot = self.hash_fun(value)
        initialSlot = slot
        while self.slots[slot] is not None:
            if self.slots[slot] == value:
                return slot
            slot = (slot + self.step) % self.size
            if slot == initialSlot:
                return None
        return None