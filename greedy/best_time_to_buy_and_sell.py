'''
Created on Oct 9, 2017

@author: eugene

array of stock prices

'''

def maxProfit(arr):
    total = 0
    for i in range(len(arr)-1):
        
        if arr[i+1] > arr[i]:
            total += arr[i+1] - arr[i]
            
    return total

arr = [138,135,140,145,130,160,175,185,190]
print maxProfit(arr)