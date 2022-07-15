import unittest

from DynArray import DynArray

def make_dyn_array(lst):
    array = DynArray()
    for i in lst:
        array.append(i)
        
    return array

def fill_dyn_array(array, lst):   
    for i in lst:
        array.append(i)
        
    return array
    


def array_values_eq(array1, array2):
    if len(array1) != len(array2):
        return False        
        
    result = True    
    for i in range(0, len(array1)):  
        if array1[i] != array2[i]:
            return False
    return result 


class TestInsert(unittest.TestCase):

    def test_insert_to_empty(self):
        val = 4                
        lstExpected = [val]
        
        actual   = DynArray()
        expected = make_dyn_array(lstExpected)        
        count,capacity = actual.count+1, actual.capacity
        
        actual.insert(0, val)
        
        self.assertTrue(array_values_eq(actual,expected))        
        self.assertEqual((count,capacity), (actual.count, actual.capacity))


    def test_insert_to_single_elem_array(self):
        val = 4
        pos = 0
        lst = [val-1]       
        lstExpected = [val]+[val-1]
        
        actual   = make_dyn_array(lst)
        expected = make_dyn_array(lstExpected)        
        count,capacity = actual.count+1, actual.capacity
        
        actual.insert(pos, val)
        
        self.assertTrue(array_values_eq(actual,expected))        
        self.assertEqual((count,capacity), (actual.count, actual.capacity))

        
    def test_insert_non_empty_not_grow_buf(self):
        N = 14
        val = N+1
        pos = 5
        
        lst = [x for x in range (0,N)]
        lstExpected = [x for x in range (0,pos)] + [val] + [x for x in range (pos,N)]
        
        actual   = make_dyn_array(lst)
        expected = make_dyn_array(lstExpected)
        count,capacity = actual.count+1, actual.capacity
        
        actual.insert(pos, val)
                
        self.assertTrue(array_values_eq(actual,expected))        
        self.assertEqual((count,capacity), (actual.count, actual.capacity))

    def test_insert_non_empty_not_grow_buf_bound(self):
        N = 15
        val = N+1
        pos = 5
        
        lst = [x for x in range (0,N)]
        lstExpected = [x for x in range (0,pos)] + [val] + [x for x in range (pos,N)]
        
        actual   = make_dyn_array(lst)
        expected = make_dyn_array(lstExpected)
        count,capacity = actual.count+1, actual.capacity
        
        actual.insert(pos, val)
                
        self.assertTrue(array_values_eq(actual,expected))        
        self.assertEqual((count,capacity), (actual.count, actual.capacity))
        
        
    def test_insert_buffer_exceeded(self):
        val = 17        
        
        actual = DynArray()
        initialCapacity = actual.capacity
        N = initialCapacity
        pos = N - 3
        
        fill_dyn_array(actual, [val-1] * N)        
        expected = make_dyn_array([val-1] * pos + [val] + [val-1] * (N-pos))
        count, capacity = N+1, initialCapacity * 2
        
        actual.insert(pos, val)
        
        self.assertTrue(array_values_eq(actual,expected))        
        self.assertEqual((actual.count, actual.capacity), (count,capacity))


    def test_insert_to_end_buffer_exceeded_(self):
        val = 17        
        
        actual = DynArray()
        initialCapacity = actual.capacity
        N = initialCapacity
        pos = N - 3
        
        fill_dyn_array(actual, [val-1] * N)        
        expected = make_dyn_array([val-1] * N + [val])
        count, capacity = N+1, initialCapacity * 2
        
        actual.insert(N, val)
        
        self.assertTrue(array_values_eq(actual,expected))        
        self.assertEqual((actual.count, actual.capacity), (count,capacity))


    def test_insert_to_invalid_pos(self):
        array = make_dyn_array([1,2,3])
        count,capacity = array.count, array.capacity
        
        self.assertRaises(IndexError, array.insert, array.count + 1, 4)
        self.assertRaises(IndexError, array.insert, -1, 4)
        self.assertEqual((count,capacity), (array.count, array.capacity))
        
    
    def test_insert_to_end(self):        
        val = 4
        lst = [1,2,3]
        
        actual   = make_dyn_array(lst)
        expected = make_dyn_array(lst+[val])
        count,capacity = actual.count+1, actual.capacity
        
        actual.insert(actual.count, val)
        
        self.assertTrue(array_values_eq(actual,expected))
        self.assertEqual((count,capacity), (actual.count, actual.capacity))

        
class TestDelete(unittest.TestCase):

    def test_delete_invalid_pos(self):
        array = make_dyn_array([1,2,3])
        count,capacity = array.count, array.capacity
        
        self.assertRaises(IndexError, array.delete, array.count + 1)
        self.assertRaises(IndexError, array.delete, array.count)
        self.assertRaises(IndexError, array.delete, -1)
        self.assertEqual((count,capacity), (array.count, array.capacity))

    
    def test_delete_no_reduce_capacity(self):
        N = 15
        pos = 4
        lst = [x for x in range(0,N)]
        lstExpected = [x for x in range(0,pos)] + [x for x in range(pos+1,N)]
        
        actual   = make_dyn_array(lst)
        expected = make_dyn_array(lstExpected)
        count, capacity = actual.count - 1, actual.capacity
        
        actual.delete(pos)
                
        self.assertTrue(array_values_eq(actual,expected))        
        self.assertEqual((count,capacity), (actual.count, actual.capacity))


    def test_delete_first_no_reduce(self):
        N = 15
        
        lst = [x for x in range(0,N)]
        lstExpected = [x for x in range(1,N)]
        
        actual   = make_dyn_array(lst)
        expected = make_dyn_array(lstExpected)
        count, capacity = actual.count - 1, actual.capacity
        
        actual.delete(0)
        
        self.assertTrue(array_values_eq(actual,expected))        
        self.assertEqual((count,capacity), (actual.count, actual.capacity))


    def test_delete_last_no_reduce(self):
        N = 15
        val = N
        
        lst = [x for x in range(0,N)] + [N]
        lstExpected = [x for x in range(0,N)]
        
        actual   = make_dyn_array(lst)
        expected = make_dyn_array(lstExpected)
        count, capacity = actual.count - 1, actual.capacity
        
        actual.delete(N)
        
        self.assertTrue(array_values_eq(actual, expected))        
        self.assertEqual((count,capacity), (actual.count, actual.capacity))

    def test_delete_next_to_last_no_reduce(self):
        N = 15
        val = N
        
        lst = [x for x in range(0,N)] + [N]
        lstExpected = [x for x in range(0,N-1)] + [N]
        
        actual   = make_dyn_array(lst)
        expected = make_dyn_array(lstExpected)
        count, capacity = actual.count - 1, actual.capacity
        
        actual.delete(N-1)

        self.assertTrue(array_values_eq(actual, expected))        
        self.assertEqual((count,capacity), (actual.count, actual.capacity))  
    
    
    def test_delete_one_elem(self):        
        val = 4        
        lst = [val]        
        
        actual   = make_dyn_array(lst)
        expected = DynArray()
        
        count,capacity = 0, 16
        
        actual.delete(0)
        
        self.assertTrue(array_values_eq(actual, expected))        
        self.assertEqual((count,capacity), (actual.count, actual.capacity))
    
    def test_delete_reduce_capacity(self):
        N = 32
        pos = 12
        
        lst = [x for x in range(0,N)]
        lstExpected = [x for x in range(0,pos)] + [x for x in range(pos+1,N)]
        
        actual   = make_dyn_array(lst)
        actual.resize(N*2)
        
        expected = make_dyn_array(lstExpected)
        
        count, capacity = actual.count - 1, int(actual.capacity / 1.5)
        
        actual.delete(pos)

        self.assertTrue(array_values_eq(actual, expected))        
        self.assertEqual((count,capacity), (actual.count, actual.capacity))          

    def test_delete_no_reduce_capacity(self):
        N = 33
        pos = 15
        
        lst = [x for x in range(0,N)]
        lstExpected = [x for x in range(0,pos)] + [x for x in range(pos+1,N)]
        
        actual   = make_dyn_array(lst)        
        actual.resize((N-1)*2)
        
        expected = make_dyn_array(lstExpected)
        
        count, capacity = actual.count - 1, actual.capacity
        
        actual.delete(pos)

        self.assertTrue(array_values_eq(actual, expected))        
        self.assertEqual((count,capacity), (actual.count, actual.capacity))

        
    def test_delete_leave_minimal_capacity(self):
        resize_size = int((16 * 2) / 1.5)
        N = resize_size // 2
        pos = N-2
        
        lst = [x for x in range(0,N)]
        lstExpected = [x for x in range(0,pos)] + [x for x in range(pos+1,N)]
        
        actual = make_dyn_array(lst)                
        actual.resize(resize_size)       
        expected = make_dyn_array(lstExpected)        
        count, capacity = actual.count - 1, 16
        
        actual.delete(pos)

        self.assertTrue(array_values_eq(actual, expected))        
        self.assertEqual((count,capacity), (actual.count, actual.capacity))
        