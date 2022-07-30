import unittest
import time 

from PowerSet import PowerSet

def init_set(elems):
    s = PowerSet()
    for elem in elems:
        s.put(elem)
    return s 

def are_sets_equal(set1,set2):
    return set1.container == set2.container
    

class TestPutGet(unittest.TestCase):
    def test_get_empty(self):
        pwrSet = PowerSet()
        val = 'abc'
        self.assertFalse(pwrSet.get(val))
        self.assertEqual(pwrSet.size(), 0)
        
    def test_get_exisiting(self):
        pwrSet = PowerSet()
        val = 'abc'
        pwrSet.put(val)
        self.assertTrue(pwrSet.get(val))
        self.assertEqual(pwrSet.size(),1)
    
    def test_double_put(self):
        pwrSet = PowerSet()
        val = 'abc'
        pwrSet.put(val)
        pwrSet.put(val)
        self.assertTrue(pwrSet.get(val))
        self.assertEqual(pwrSet.size(),1)
        
    def test_put_multiple(self):
        val = 'a'
        N = 10
        pwrSet = PowerSet()
        values = [val*x for x in range(N)]
        for val in values:
            pwrSet.put(val)
        for val in values:
            self.assertTrue(pwrSet.get(val))       
        self.assertEqual(pwrSet.size(), N)

    
class TestRemove(unittest.TestCase):
    def test_remove_empty(self):
        pwrSet = PowerSet()
        val = 'abc'
        self.assertFalse(pwrSet.remove(val))
        self.assertEqual(pwrSet.size(), 0)

    def test_remove_existing(self):
        pwrSet = PowerSet()
        val = 'abc'
        pwrSet.put(val)        
        self.assertTrue(pwrSet.remove(val))
        self.assertEqual(pwrSet.size(), 0)

    def test_remove_existing(self):
        pwrSet = PowerSet()
        val = 'abc'
        pwrSet.put(val)        
        self.assertTrue(pwrSet.remove(val))
        self.assertFalse(pwrSet.get(val))
        self.assertEqual(pwrSet.size(), 0)

    def test_put_multiple(self):
        val = 'a'
        N = 10
        pwrSet = PowerSet()
        values = [val*x for x in range(N)]
        for val in values:
            pwrSet.put(val)
        self.assertTrue(pwrSet.remove(values[0]))
        self.assertFalse(pwrSet.get(values[0]))
        self.assertEqual(pwrSet.size(), N-1)

    
class TestIntersection(unittest.TestCase):

    def test_intersection_empty(self):
        val = 'a'
        N = 10
        values = [val*x for x in range(N)]
        set1 = init_set(values)
        set2 = PowerSet()
        intersection = set1.intersection(set2)
        self.assertEqual(intersection.size(), 0)
        
    def test_intersection_non_empty(self):
        N = 7
        dif = 3
        set1 = init_set([x for x in range(N)])
        set2 = init_set([x for x in range(N-dif,N+dif)])
        expected = init_set([x for x in range(N-dif,N)])
        actual = set1.intersection(set2)
        self.assertTrue(are_sets_equal(expected, actual))
        self.assertEqual(actual.size(), dif)
    
    def test_empty_intersection(self):
        N = 7       
        set1 = init_set([x for x in range(N)])
        set2 = init_set([x for x in range(N,2*N)])
        expected = PowerSet()
        actual = set1.intersection(set2)
        self.assertTrue(are_sets_equal(expected, actual))
        self.assertEqual(actual.size(), 0)
    
    def test_intersection_fast_enough(self):
        N = 20000
        dif = 5000
        set1 = init_set([x for x in range(N)])
        set2 = init_set([x for x in range(N-dif,N+dif)])
        expected = init_set([x for x in range(N-dif,N)])
        
        startTime = time.time()
        actual = set1.intersection(set2)
        endTime = time.time()
        self.assertTrue(are_sets_equal(expected, actual))
        self.assertEqual(actual.size(), dif)
        self.assertTrue(endTime - startTime < 3)


class TestUnion(unittest.TestCase):
    
    def test_union_of_empty_sets(self):
        set1 = PowerSet()
        set2 = PowerSet()
        union = set1.union(set2)
        self.assertTrue(are_sets_equal(set1, union))
    
    def test_union_with_empty_sets(self):
        val = 'a'
        N = 10
        values = [val*x for x in range(N)]
        set1 = init_set(values)
        set2 = PowerSet()
        union = set1.union(set2)
        self.assertTrue(are_sets_equal(set1, union))
    
    def test_union_non_intersecting_sets(self):
        N = 10
        set1 = init_set([x for x in range(N)])
        set2 = init_set([x for x in range(N, 2*N)])
        expected = init_set([x for x in range(0, 2*N)])
        union = set1.union(set2)
        self.assertTrue(are_sets_equal(expected, union))
    
    def test_union_intersecting_sets(self):
        N = 10
        set1 = init_set([x for x in range(2*N)])
        set2 = init_set([x for x in range(N, 3*N)])
        expected = init_set([x for x in range(0, 3*N)])
        union = set1.union(set2)
        self.assertTrue(are_sets_equal(expected, union))
    
    def test_union_fast_enough(self):
        N = 10000
        set1 = init_set([x for x in range(2*N)])
        set2 = init_set([x for x in range(N, 3*N)])
        expected = init_set([x for x in range(0, 3*N)])
        
        startTime = time.time()
        actual = set1.union(set2)
        endTime = time.time()
        self.assertTrue(are_sets_equal(expected, actual))
        self.assertTrue(endTime - startTime < 3)


class TestDifference(unittest.TestCase):
    
    def test_dif_empty_sets(self):
        set1 = PowerSet()
        set2 = PowerSet()
        diff = set1.difference(set2)
        self.assertTrue(are_sets_equal(set1, diff))
    
    def test_dif_empty_and_non_empty(self):
        N = 10
        set1 = init_set([x for x in range(N)])
        set2 = PowerSet()
        expected = init_set([x for x in range(N)])
        diff = set1.difference(set2)
        self.assertTrue(are_sets_equal(expected, diff))
    
    def test_dif_empty_and_non_empty(self):
        N = 10
        set1 = PowerSet()
        set2 = init_set([x for x in range(N)])
        expected = PowerSet()
        diff = set1.difference(set2)
        self.assertTrue(are_sets_equal(expected, diff))

    def test_dif_non_intersecting(self):
        N = 10
        set1 = init_set([x for x in range(N)])
        set2 = init_set([x for x in range(N, 2*N)])
        expected = init_set([x for x in range(0, N)])
        diff = set1.difference(set2)
        self.assertTrue(are_sets_equal(expected, diff))

    def test_dif_intersecting(self):
        N = 10
        set1 = init_set([x for x in range(2*N)])
        set2 = init_set([x for x in range(N, 3*N)])
        expected = init_set([x for x in range(N)])
        diff = set1.difference(set2)
        self.assertTrue(are_sets_equal(expected, diff))

    def test_dif_fast_enough(self):
        N = 20000
        set1 = init_set([x for x in range(2*N)])
        set2 = init_set([x for x in range(N, 3*N)])
        expected = init_set([x for x in range(N)])
        startTime = time.time()
        diff = set1.difference(set2)
        endTime = time.time()
        self.assertTrue(are_sets_equal(expected, diff))       
        self.assertTrue(endTime - startTime < 3)


class TestSubset(unittest.TestCase):

    def test_subset_of_empty_set(self):
        set1 = PowerSet()
        set2 = PowerSet()
        self.assertFalse(set1.issubset(set2))
    
    def test_subset_of_empty_set(self):
        N = 10
        set1 = PowerSet()
        set2 = init_set([x for x in range(N)])
        self.assertFalse(set2.issubset(set1))

    def test_empty_set_is_always_subset(self):
        N = 10
        set1 = init_set([x for x in range(N)])
        set2 = PowerSet()
        self.assertTrue(set2.issubset(set1))

    def test_subset_non_intersecting(self):
        N = 11
        set1 = init_set([x for x in range(N)])
        set2 = init_set([x for x in range(N, 2*N)])
        self.assertFalse(set2.issubset(set1))
        self.assertFalse(set1.issubset(set2))

    def test_subset_intersecting(self):
        N = 11
        set1 = init_set([x for x in range(2*N)])
        set2 = init_set([x for x in range(N, 3*N)])
        self.assertFalse(set2.issubset(set1))
        self.assertFalse(set1.issubset(set2))

    def test_subset(self):
        N = 11
        set1 = init_set([x for x in range(N)])
        set2 = init_set([x for x in range(0, 3*N)])
        self.assertFalse(set2.issubset(set1))
        self.assertTrue(set1.issubset(set2))
        
    def test_subset_fast_enough(self):
        N = 20000
        set1 = init_set([x for x in range(N)])
        set2 = init_set([x for x in range(0, 3*N)])
        startTime = time.time()
        self.assertFalse(set2.issubset(set1))
        self.assertTrue(set1.issubset(set2))
        endTime = time.time()
        self.assertTrue(endTime - startTime < 3)