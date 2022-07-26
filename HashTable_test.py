import unittest

from HashTable import HashTable

class TestSeekSlot(unittest.TestCase):
    
    def test_seek_slot_empty(self):
        tab = HashTable(sz = 37, stp = 3)
        val = 'abc'        
        slot = tab.seek_slot(val)
        self.assertEqual(slot, tab.hash_fun(val))
    
    def test_seek_slot_collision(self):
        tab = HashTable(sz = 37, stp = 3)
        val1 = 'abc'
        slot1 = tab.seek_slot(val1)
        tab.slots[slot1] = val1        
        val2 = '#'
        slot2 = tab.seek_slot(val2)
        self.assertEqual(slot2, (tab.hash_fun(val2) + tab.step) % tab.size)
    
    def test_seek_slot_full_table(self):
        size = 4
        step = 2
        tab = HashTable(sz = size, stp = step)
        val = 36
        values = [chr(val + i*step) for i in range (size//step)]        
        for v in values:
            tab.slots[tab.seek_slot(v)] = v        
        valueToInsert = chr(ord(values[-1]) + step)        
        self.assertEqual(tab.seek_slot(valueToInsert), None)

    def test_seek_slot_full_table_2(self):
        size = 5
        step = 2
        tab = HashTable(sz = size, stp = step)
        val = 36
        values = [chr(val + i*step) for i in range (size)]        
        for v in values:
            tab.slots[tab.seek_slot(v)] = v        
        valueToInsert = chr(ord(values[-1]) + step)        
        self.assertEqual(tab.seek_slot(valueToInsert), None)


class TestPut(unittest.TestCase):
    
    def test_put_into_empty_table(self):
        size = 5
        step = 2
        tab = HashTable(sz = size, stp = step)
        val = chr(36)
        tab.put(val)
        self.assertEqual(tab.slots[tab.hash_fun(val)], val)
        
    def test_put_one_collision(self):
        size = 5
        step = 2
        tab = HashTable(sz = size, stp = step)
        val1 = chr(36)
        slot1 = tab.put(val1)        
        val2 = chr(36+step)
        slot2 = tab.put(val2)
        self.assertEqual(tab.slots[slot1], val1)
        self.assertEqual(tab.slots[slot2], val2)
    
    def test_put_no_free_elements(self):
        size = 5
        step = 2
        tab = HashTable(sz = size, stp = step)
        val = 36
        values = [chr(val + i*step) for i in range (size)]        
        for v in values:
            tab.put(v)
        valToPut = chr(ord(values[-1]) + step)
        slot = tab.put(valToPut)
        self.assertEqual(slot, None)        
    
    def test_put_the_same_value(self):
        size = 5
        step = 2
        tab = HashTable(sz = size, stp = step)
        val = chr(36)
        slot1 = tab.put(val)                
        slot2 = tab.put(val)
        self.assertEqual(tab.slots[slot1], val)
        self.assertEqual(slot1, slot2)


class TestFind(unittest.TestCase):
    
    def test_find_empty(self):
        size = 5
        step = 2
        tab = HashTable(sz = size, stp = step)
        valToFind = chr(37)
        valIndex = tab.find(valToFind)
        self.assertEqual(valIndex, None)
        
    def test_find_absent(self):
        size = 5
        step = 2
        tab = HashTable(sz = size, stp = step)
        val = 36
        values = [chr(val + i*step) for i in range (size)]        
        for v in values:
            tab.put(v)
        valToFind = chr(ord(values[-1]) + step)
        slot = tab.find(valToFind)
        self.assertEqual(slot, None)

    def test_find_single(self):
        size = 5
        step = 2
        tab = HashTable(sz = size, stp = step)
        val = chr(36)
        slotExpected = tab.put(val)
        slotFound = tab.find(val)
        self.assertEqual(slotExpected, slotFound)       
    
    def test_find_several_no_collisions(self):
        size = 5
        step = 2
        tab = HashTable(sz = size, stp = step)
        val = 37
        values = [chr(val + i*step) for i in range (size)]        
        slotsActual  = []        
        slotsExpected  = []        
        for v in values[:-2:]:
            slotsActual.append(tab.put(v))
        for v in values[:-2:]:
            slotsExpected.append(tab.find(v))         
        self.assertEqual(slotsExpected, slotsActual)
        
    def test_find_full_table(self):
        size = 4
        step = 2
        tab = HashTable(sz = size, stp = step)
        val = 36
        values = [chr(val + i*step) for i in range (size//step)]
        slotsActual = []
        for v in values:
            slotsActual.append(tab.put(v))
        slotExpected = tab.find(values[-1])     
        self.assertEqual(slotExpected, slotsActual[-1])
    
    def test_find_collisions(self):
        size = 20
        step = 3
        tab = HashTable(sz = size, stp = step)
        rem = 3
        val1 = chr(size*2 + rem)
        tab.put(val1)
        val2 = chr(size*3 + rem)
        slotExpected = tab.put(val2)
        slotActual = tab.find(val2)
        self.assertEqual(slotExpected, slotActual)

    def test_find_several_collisions(self):
        size = 20
        step = 3
        tab  = HashTable(sz = size, stp = step)
        rem  = 3
        val1 = chr(size*2 + rem)
        tab.put(val1)
        val2 = chr(size*3 + rem)
        slotExpected = tab.put(val2)
        slotActual = tab.find(val2)
        self.assertEqual(slotExpected, slotActual)
    
    def test_find_absent_collisions(self):
        size = 17
        step = 3
        tab  = HashTable(sz = size, stp = step)
        rem = 1
        values = [chr(size*i + rem) for i in range ((size//step) + 1)]
        slots = []
        for v in values:
            slots.append(tab.put(v))
        val = chr(ord(values[-1]) + size)
        slotActual = tab.find(val)
        self.assertEqual(slotActual, None)
    
    def test_find_last_collisions(self):
        size = 17
        step = 3
        tab  = HashTable(sz = size, stp = step)
        rem = 1
        values = [chr(size*i + rem) for i in range ((size//step))]
        slots = []
        for v in values[:-1:]:
            slots.append(tab.put(v))
        val = values[-2]
        slotActual = tab.find(val)
        self.assertEqual(slotActual, slots[-1])