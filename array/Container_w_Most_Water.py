'''
Created on Sep 27, 2017

@author: eugenep

Given n non-negative ints a1, a2, ..., an where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i,0)

Find two lines, which together with x-axis forms a container, such that the container contains the most water

given [2, 7, 5, 9, 15, 4]




           |
           |
           |
x-axis     |---|---|---|---|---|---|

water = l * height (smaller of the two)
'''

def get_water(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    
    length = abs(x1 - x2)
    height = min(y1, y2)
    return length * height

def find_most_water(arr):
    # exhaustive O(N^2)
    
    max_water = 0
    max_water_lines = None
    for i, n in enumerate(arr):
        for j, m in enumerate(arr):
            if i == j:
                continue
            else:
                w = get_water( (i, n), (j, m) )
                if w > max_water:
                    max_water = w
                    max_water_lines = [n, m]
                    
    return max_water_lines
        
def find_most_water_ptrs(arr):
    # O(N)
    left = 0
    right = len(arr) - 1
    
    max_water_lines = None
    max = 0
    while left < right:
        w = (right - left) * min(arr[left], arr[right])
        if w > max:
            max = w
            max_water_lines = [arr[left], arr[right]]
        
        if arr[left] > arr[right]:
            right -= 1
        else:
            left += 1

    return max_water_lines

arr = [2, 7, 5, 9, 15, 4]

print find_most_water(arr)
print find_most_water_ptrs(arr)




