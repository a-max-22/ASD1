import unittest

from NativeCache import NativeCache

def put_multiple_values(dct, keys, vals):
    for key,val in zip(keys,vals):
        dct.put(key,val)                   

def get_multiple_values(dct, keys):
    actualValues = []    
    for key in keys:
        actualValues.append(dct.get(key))
    return actualValues

def get_collision_for_key(dct, key):
    hashVal = dct.hash_fun(key)
    size = dct.size
    addend = size // len(key)
    newKey = ''
    for k in key[:-1:]:
        newKey += chr(ord(k)+addend)
    newKey += chr(ord(key[-1])+ size - (addend*len(key[:-1:])))        
    if dct.hash_fun(key) != dct.hash_fun(newKey):
        raise ValueError('No collision', dct.hash_fun(key), dct.hash_fun(newKey))
    
    return newKey

class TestPutGet(unittest.TestCase):
    
    def test_put_single(self):
        dct = NativeCache(sz = 5)
        val = 3
        dct.put('abc', val)
        slot = dct.find('abc')
        self.assertEqual(dct.slots[slot], 'abc')
        self.assertEqual(dct.values[slot], val)


    def test_put_multiple_no_collision(self):
        size = 5
        dct = NativeCache(sz = size)
        vals = [x for x in range(size)]
        keys = [chr(x+35) for x in vals]
        put_multiple_values(dct, keys,vals)        
        actualValues = get_multiple_values(dct, keys)
        self.assertEqual(actualValues, vals)
    
    def test_put_value_collision(self):
        size = 5
        dct = NativeCache(size)
        key = 'ab'
        val = 2
        cKey = get_collision_for_key(dct, key)
        cVal = val + 1
        dct.put(key,val)
        dct.put(cKey, cVal)
        self.assertEqual(dct.get(key),val)
        self.assertEqual(dct.get(cKey),cVal)

    def test_put_value_one_collision_free_slot_left(self):
        size = 3
        dct = NativeCache(size)
        vals = [x for x in range(size-1)]
        keys = ['a'+chr(x+35) for x in vals]
        put_multiple_values(dct, keys, vals)
        collisionKey = get_collision_for_key(dct, keys[0])
        collisionVal = size
        dct.put(collisionKey, collisionVal)
        
        actualValues = get_multiple_values(dct, keys+[collisionKey])
        self.assertEqual(actualValues, vals+[collisionVal])
        self.assertEqual(collisionVal, dct.get(collisionKey))

    def test_put_value_multiple_collisions(self):
        size = 5
        dct = NativeCache(size)
        vals = [x for x in range(size-1)]
        keys = ['a'+chr(x*size+2) for x in vals]
        put_multiple_values(dct, keys, vals)
        actualValues = get_multiple_values(dct, keys)
        self.assertEqual(actualValues, vals)

    def test_put_value_not_enough_space(self):
        size = 5
        dct = NativeCache(sz = size)
        vals = [x for x in range(size)]
        keys = [chr(x+35) for x in vals]
        put_multiple_values(dct, keys,vals)        
        newKey = chr(ord(keys[-1])+size)
        newVal = size+1
        dct.put(newKey, newVal)        
        actualValues = get_multiple_values(dct, keys[:-1:]+[newKey])
        self.assertEqual(actualValues, vals[:-1:]+[newVal])        

    def test_put_value_pop_elem_with_min_hits(self):
        size = 5
        dct = NativeCache(sz = size)
        vals = [x for x in range(size)]
        keys = [chr(x+35) for x in vals]
        put_multiple_values(dct, keys,vals)        
        
        desired_hits_count = 0
        for key,val in zip(keys,vals):
            for c in range(desired_hits_count):                
                self.assertEqual(dct.get(key), val)
            desired_hits_count += 1
            
        newKey = chr(ord(keys[-1])+size)
        newVal = size+1
        dct.put(newKey, newVal)        
        
        actualValues = get_multiple_values(dct, [newKey]+keys[1::])
        self.assertEqual(actualValues, [newVal]+vals[1::])        
        