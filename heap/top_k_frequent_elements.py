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
            if bucket[freq] is None:
                bucket[freq] = []
            bucket[freq].append[ele]
        
        for i in reverse(range(bucket)):
            print i
        
        return


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()