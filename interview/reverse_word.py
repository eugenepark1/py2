'''
Created on Aug 8, 2018

@author: eugene


Input: "the sky is blue",
Output: "blue is sky the".

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
'''

import re


def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(re.compile('\S+').findall(s)[::-1])
    
print reverseWords("the sky is blue")