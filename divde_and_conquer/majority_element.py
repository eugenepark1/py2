'''
Created on Oct 8, 2017

@author: eugene
majority element is the element which appears more than n/2 times where n is the length of array
'''

def majority_element(arr):
    
    major = arr[0]
    count = 1
    
    for i in range(1, len(arr)):
        
        
        if count == 0:
            count += 1
            major = arr[i] # new major
        elif (major == arr[i]):
            count += 1
        else:
            count -= 1
        
        print "major: %s (%s)" % (major, count)

    return major


arr = [1,2,2,3,4,5,1,1,1,1,1,1]
print majority_element(arr)
