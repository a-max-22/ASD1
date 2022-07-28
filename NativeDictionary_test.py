import unittest

from NativeDictionary import NativeDictionary

def put_multiple_values(dct, keys, vals):
    for key,val in zip(keys,vals):
        dct.put(key,val)                   

def get_multiple_values(dct, keys, vals):
    actualValues = []    
    for key in keys:
        actualValues.append(dct.get(key))
    return actualValues


class TestPutGet(unittest.TestCase):
    
    def test_put_single(self):
        dct = NativeDictionary(sz = 5)
        val = 3
        dct.put('abc', val)
        slot = dct.find('abc')
        self.assertEqual(dct.slots[slot], 'abc')
        self.assertEqual(dct.values[slot], val)

    def test_put_multiple_no_collision(self):
        size = 5
        dct = NativeDictionary(sz = size)
        vals = [x for x in range(size)]
        keys = [chr(x+35) for x in vals]
        put_multiple_values(dct, keys,vals)        
        actualValues = get_multiple_values(dct, keys, vals)
        self.assertEqual(actualValues, vals)
        
    def test_put_value_one_collision_free_slot_left(self):
        size = 6
        dct = NativeDictionary(size)
        vals = [x for x in range(size-1)]
        keys = [chr(x+35) for x in vals]
        put_multiple_values(dct, keys,vals)
        collisionKey = chr(ord(keys[0]) + size)
        collisionVal = size
        dct.put(collisionKey, collisionVal)
        actualValues = get_multiple_values(dct, keys, vals)
        self.assertEqual(actualValues, vals)
        self.assertEqual(collisionVal, dct.get(collisionKey))
    
    def test_put_value_multiple_collisions(self):
        size = 5
        dct = NativeDictionary(size)
        vals = [x for x in range(size-1)]
        keys = [chr(x*size+2) for x in vals]
        put_multiple_values(dct, keys, vals)
        actualValues = get_multiple_values(dct, keys, vals)
        self.assertEqual(actualValues, vals)
    
    def test_put_value_not_enough_space(self):
        size = 5
        dct = NativeDictionary(sz = size)
        vals = [x for x in range(size)]
        keys = [chr(x+35) for x in vals]
        put_multiple_values(dct, keys,vals)        
        actualValues = get_multiple_values(dct, keys, vals)
        self.assertEqual(actualValues, vals)
        newKey = chr(ord(keys[-1])+1)
        newVal = 0
        self.assertRaises(KeyError, dct.put, newKey, newVal)
        
        
class TestisKey(unittest.TestCase):
    
    def test_key_in_dct(self):
        size = 5
        dct = NativeDictionary(sz = size)
        key = 'abc'
        dct.put(key, 0)
        self.assertTrue(dct.is_key(key))

    def test_key_in_empty_dct(self):
        size = 5
        dct = NativeDictionary(sz = size)
        key = 'abc'        
        self.assertFalse(dct.is_key(key))

    def test_multiple_keys_in_dct(self):
        size = 5
        dct = NativeDictionary(sz = size)
        vals = [x for x in range(size)]
        keys = [chr(x+35) for x in vals]
        put_multiple_values(dct, keys,vals)        
        for key in keys:
            self.assertTrue(dct.is_key(key))
    
    def test_absent_key_in_dict_collision(self):
        size = 5
        dct = NativeDictionary(size)
        vals = [x for x in range(size-1)]
        keys = [chr(x*size+2) for x in vals]
        put_multiple_values(dct, keys, vals)
        newKey = chr(ord(keys[-1])+size)
        self.assertFalse(dct.is_key(newKey))
    