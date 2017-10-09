'''
Created on Oct 2, 2017

@author: eugenep

1) sort the array - O(N lg N)
2) min-heap O(N log k)
3) selection algo based on the partition method - the same used for quicksort
    O(N) best O(N^2) worst
    randomized input to guarantee O(n)
'''
import unittest
import heapq


class Test(unittest.TestCase):


    def testName(self):
        pass

    def test_kth_largest_heap(self):
        arr = [5,7,3,2,9]
        
        heapq.heapify(arr)
        
        k = 3
        k_popped = []
        for i in range(3):
            k_popped.append(heapq.heappop(arr))
        
        expected = [2,3,5]
        self.assertItemsEqual(expected, k_popped, "expected: %s actual: %s" % (expected, k_popped))
        
        return


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()