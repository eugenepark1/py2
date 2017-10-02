'''
Created on Oct 2, 2017

@author: eugenep

design a data structure that supports all following ops in avg O(1) time

insert(val)
remove(val)
getRandom(val) - each element has the same probabilbiy 

no duplicatesd
'''
import random

tmp_dict = {}
new_ds = []
def insert(item):
    if item not in tmp_dict:
        index = len(new_ds)
        new_ds.append(item)
        tmp_dict[item] = index
        return True
    else:
        return False
        

def remove(item):
    global new_ds
    if item in tmp_dict:
        index_to_remove = tmp_dict[item]
        # bring the last time to this index
        new_ds[index_to_remove] = new_ds[-1]
        tmp_dict[new_ds[index_to_remove]] = index_to_remove
        new_ds = new_ds[:-1]
        del tmp_dict[item]
        return True
    else:
        return False

def getRandom():
    global  new_ds
    maxlen = len(new_ds)-1
    
    if maxlen > 0:
        randint = random.randint(0, maxlen)
        return new_ds[randint]
    else:
        return new_ds[0]

print insert(1)
print new_ds
print remove(2)
print new_ds
print insert(2)
print new_ds
print remove(2)
print new_ds
print getRandom()
print remove(1)
print new_ds
print insert(1)
print new_ds
print getRandom()