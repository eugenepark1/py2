'''
Created on May 6, 2018

@author: eugen
'''





numOne = [1,5,8]
numTwo = [3,5,6,7]

numOne = list(numOne.reverse())
numTwo = list(numTwo.reverse())

sum = 0
for i in range(max(len(numOne), len(numTwo))):
    try:
        to_add = (numOne[i] + numTwo[i]) * 10**i
        sum += to_add
        print "%s %s %s %s" % (numOne[i], numTwo[i], i, to_add)
    except IndexError:
        # need to do something
        if i < len(numOne):
            to_add =  numOne[i] * 10**i
        else:
            to_add = numTwo[i] * 10**i
        sum += to_add
        
print sum