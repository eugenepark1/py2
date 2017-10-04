'''
Created on Oct 3, 2017

@author: eugenep
two int arrs: nums1 and nums2 sorted in ascending order 
and int k

define a pair(u,v) which consists of one element from the first and one element from the second

find k pairs w/ the smallest sums
(u1, v1), (u2, v2),...,(uk,vk) with the smallest sums

nums1 [1,7,11]
nums2 [2,4,6]
k=3
return [1,2], [1,4], [1,6]

nums1 [1,1,2]
nums2[2,4,6]
k=2
return [1,1], [1,1]
'''
import unittest
from heapq import heappush,heappop


class Test(unittest.TestCase):


    def testName(self):
        pass
    
    def test_sum_two_arrs(self):
        nums1 = [1,7,11]
        nums2 = [2,4,6]
        
        # 1, 2
        # 1, 4
        # 1, 6
        # 7, 2
        # 7, 4
        # 7, 6
        #...
        
        k = 3
        h = []
        for i, ele1 in enumerate(nums1):
            for j, ele2 in enumerate(nums2):
                sum = ele1 + ele2
                heappush(h, (ele1+ele2, (ele1, ele2)))
        
        res = []
        for i in range(k):
            res.append(heappop(h)[1])
            
        expected = [(1,2), (1,4), (1,6)]
        
        self.assertItemsEqual(expected, res, "")
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()