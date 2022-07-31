class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.mask_unit_size = 32
        self.filter_mask = 0

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
    
    def get_bitmask(self, pos):
        if pos > self.filter_len or pos < 0:
            raise IndexError('Position is outside of bitfield bounds')
        bitMask   = 1 << pos
        return bitMask
        
    def set_bit(self, pos):
        bitMask = self.get_bitmask(pos)        
        self.filter_mask = self.filter_mask | bitMask
    
    def is_bit_set(self, pos):
        bitMask = self.get_bitmask(pos)        
        return (self.filter_mask & bitMask) != 0
    
    def add(self, str1):
        p1 = self.hash1(str1)
        p2 = self.hash2(str1)
        self.set_bit(p1)
        self.set_bit(p2)                

    def is_value(self, str1):
        p1 = self.hash1(str1)
        p2 = self.hash2(str1)        
        return self.is_bit_set(p1) and self.is_bit_set(p2)
        