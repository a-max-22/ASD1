class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.mask_unit_size = 32
        self.filter_mask = [0]*(f_len // self.mask_unit_size)

    def general_hash(self, key, val):
        res = 0
        for c in val:
            code = ord(c)
            res = (res*key + code) % self.filter_len
        return res

    def hash1(self, str1):
        return self.general_hash(17, str1)

    def hash2(self, str1):
        return self.general_hash(223, str1)
    
    def get_unit_index_and_bitmask(self, pos):
        if pos > self.filter_len or pos < 0:
            raise IndexError('Position is outside of bitfield bounds')
        unitIndex = pos // self.mask_unit_size        
        bitPos    = pos % self.mask_unit_size        
        unit      = self.filter_mask[unitIndex]
        bitMask   = 1 << bitPos
        return (unitIndex, bitMask)
        
    def set_bit(self, pos):
        unitIndex, bitMask = self.get_unit_index_and_bitmask(pos)        
        self.filter_mask[unitIndex] = self.filter_mask[unitIndex] | bitMask
    
    def is_bit_set(self, pos):
        unitIndex, bitMask = self.get_unit_index_and_bitmask(pos)        
        return (self.filter_mask[unitIndex] & bitMask) != 0
    
    def add(self, str1):
        p1 = self.hash1(str1)
        p2 = self.hash2(str1)
        self.set_bit(p1)
        self.set_bit(p2)                

    def is_value(self, str1):
        p1 = self.hash1(str1)
        p2 = self.hash2(str1)        
        return self.is_bit_set(p1) and self.is_bit_set(p2)
        