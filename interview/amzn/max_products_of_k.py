'''
Created on Sep 18, 2018

@author: eugenep
'''


def calculate_max_product_k(arr, k):
    if k > len(arr):
        raise Exception("k is bigger than len(arr): %s %s" % (k, len(arr)))
    
    max_products_k = []
    arr = sorted(arr)
    i,j = 0, len(arr)-1
    
    while len(max_products_k) < k:
        left_product = arr[i] * arr[i+1]
        right_product = arr[j] * arr[j-1]
        
        if k-len(max_products_k) == 1:
            if arr[i] > arr[j]:
                max_products_k.append(arr[i])
            else:
                max_products_k.append(arr[j])
        else:
            if left_product > right_product:
                max_products_k += [arr[i], arr[i+1]]
                i += 2
            else:
                max_products_k += [arr[j-1], arr[j]]
                j -= 2
    return max_products_k


myArr = [-10,-8,-5,1,2,3,9]
myK = 4
print calculate_max_product_k(myArr, myK)