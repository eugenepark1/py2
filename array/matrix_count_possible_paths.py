'''
Created on Jun 26, 2018

@author: eugene

The problem is to count all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell you can either move only to right or down

https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/
https://www.geeksforgeeks.org/minimum-cost-path-left-right-bottom-moves-allowed/
https://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/
https://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/
https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-using-set-in-stl/
https://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/
https://www.geeksforgeeks.org/?p=27455

https://www.geeksforgeeks.org/longest-decreasing-subsequence/
https://www.geeksforgeeks.org/given-array-strings-find-strings-can-chained-form-circle/
https://www.geeksforgeeks.org/total-number-of-decreasing-paths-in-a-matrix/
https://www.geeksforgeeks.org/check-if-array-sum-can-be-made-k-by-three-operations-on-it/
https://www.geeksforgeeks.org/smallest-number-with-given-sum-of-digits-and-sum-of-square-of-digits/
'''
import random
def create_grid(rows, cols):
    grid = []
    for i in range(rows):
        grid.append([random.randint(1,9) for i in range(cols)])
        
    return grid

def print_grid(grid):
    for i in grid:
        print i


grid = create_grid(3, 3)
print_grid(grid)


def count_paths(x,y,xx,yy):
    if x == xx and y == yy:
        return 1
    elif x > xx or y < yy:
        return 0
    else:
        # move right or down
        return count_paths(x+1,y, xx, yy) + count_paths(x, y-1, xx, yy)

def sum_min_path(x,y, xx,yy):
    try:
        print "im at (%s, %s) w/ value %s" % (x, y, grid[x][y])
    except:
        pass
    
    if x == xx and y == yy:
        print "DEST returning %s for %s %s" % (grid[xx][yy], x, y)
        return grid[xx][yy]
    elif x > xx or y < yy:
        print 'returning 0 for %s %s' % (x,y)
        return 0
    else:
        min_value = min(sum_min_path(x+1,y, xx, yy), sum_min_path(x, y-1, xx, yy))
        print "returning %s + %s" % (min_value, grid[x][y])
        return min_value + grid[x][y]

print count_paths(0,2, 2,0)
print sum_min_path(0,2,2,0)