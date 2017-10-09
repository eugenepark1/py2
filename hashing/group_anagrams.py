'''
Created on Oct 1, 2017

@author: eugene

given an array of strings, group anagrams together

anagram: a word, phrase, or sentence formed from another by rearranging its letters
given ["eat", "tea", "tan", "ate", "nat", "bat"]

return [
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
]

'''
import unittest

def group_anagrams(arr):

    group_dict = {}
    for word in arr:
        hashcode = str(sorted(word))
        if hashcode not in group_dict:
            group_dict[hashcode] = []
        group_dict[hashcode].append(word)
        
    group_list = [sorted(v) for k,v in group_dict.iteritems()]

    return group_list

class Test(unittest.TestCase):


    def testName(self):
        pass

    def test_anagram(self):
        arr = ["eat", "tea", "tan", "ate", "nat", "bat"]

        expected = [
                ["ate", "eat", "tea"],
                ["nat", "tan"],
                ["bat"]
            ]
        
        actual = group_anagrams(arr)

        self.assertItemsEqual(expected, actual, "")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()