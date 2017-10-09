'''
Created on Oct 8, 2017

@author: eugene

n log n
'''



#          hel              lo
#     he      l            l     o
#  h    e
#   l    e     h          o        l
# o l l 3 h




def reverse(myStr):
    
    if len(myStr) == 1:
        return myStr
    
    mid = len(myStr) / 2
    
    leftStr = myStr[:mid]
    rightStr = myStr[mid:]
    
    return reverse(rightStr) + reverse(leftStr)

print reverse("hello")