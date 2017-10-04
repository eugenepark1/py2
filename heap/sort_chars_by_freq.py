'''
Created on Oct 3, 2017

@author: eugenep

given a string, sort it in decreasing order based on the freq of chars

input: "tree"
output: "eert"
'''
import unittest


class Test(unittest.TestCase):


    def testName(self):
        pass

    def test_sort_chars_by_freq(self):
        input = "tree"
        expected = "eert"
        
        freqMap = {}
        for i in input:
            if i not in freqMap:
                freqMap[i] = 0
            freqMap[i] += 1

        bucket = []
        for ch,cnt in freqMap.iteritems():
            gap = cnt - len(bucket) + 1
            if gap > 0:
                # needs to extend bucket
                for i in range(gap):
                    bucket.append(None)
                bucket[cnt] = []

            bucket[cnt].append(ch)
        
        ret = ""
        for k,v in reversed(list(enumerate(bucket))):
            if v is not None:
                for i in v:
                    ret += i*k
        
        self.assertEqual(expected, ret, "")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()