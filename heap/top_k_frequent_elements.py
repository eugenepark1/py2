'''
Created on Oct 3, 2017

@author: eugenep
'''
import unittest
from audioop import reverse


class Test(unittest.TestCase):


    def testName(self):
        pass
    
    def test_topK_bigON(self):
        arr = [1,1,1,2,2,3]
        k = 2
        expected = [1,2]
        
        bucket = []
        freqMap = {}
        
        #freq
        for ele in arr:
            if not ele in freqMap:
                freqMap[ele] = 0
            freqMap[ele] += 1
        
        #bucket
        for ele,freq in freqMap.iteritems():
            try:
                if bucket[freq] is None:
                    bucket[freq] = []
            except IndexError:
                to_add = freq - len(bucket) + 1
                for i in range(to_add):
                    bucket.append(None)
                bucket[freq] = []
            bucket[freq].append(ele)

        
        ret = []
        for i, e in reversed(list(enumerate(bucket))):
            if len(e) < k:
                ret += e
                k -= len(e)
            else:
                e = e[:k]
                ret += e
                break

        self.assertItemsEqual(expected, ret, "")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()