import unittest

from BloomFilter import BloomFilter

class TestInternalFunctions(unittest.TestCase):
    def test_set_bit_first(self):
        flt = BloomFilter(f_len = 32)
        flt.set_bit(8)
        self.assertEqual(flt.filter_mask, 0x100)        

    def test_set_bit_second_unit(self):
        mask_len = 64
        flt = BloomFilter(f_len = mask_len)
        flt.set_bit(8+32)
        self.assertEqual(flt.filter_mask, 0x10000000000)        
    
class TestAddAndIsValue(unittest.TestCase):

    def test_add_single(self):
        flt = BloomFilter(f_len = 64)
        val = 'abc'
        flt.add(val)
        self.assertTrue(flt.is_value(val))
        
    def test_add_multiple(self):
        flt = BloomFilter(f_len = 32)
        for i in range(10):
            string = ''
            for c in [str(x%10) for x in range(i,i+10)]:
                string += c            
            flt.add(string)
            self.assertTrue(flt.is_value(string))
            