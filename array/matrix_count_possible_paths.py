'''
Created on Jun 26, 2018

@author: eugene

The problem is to count all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell you can either move only to right or down
'''

def create_grid(rows, cols):
    grid = []
    for i in range(rows):
        grid.append(['X' for i in range(cols)])
        
    return grid

def print_grid(grid):
    for i in grid:
        print ' '.join(i)


grid = create_grid(3, 3)
print_grid(grid)


def count_paths(x,y,xx,yy):
    print "%s %s" % (x,y)
    if x == xx and y == yy:
        return 1
    elif x > xx or y < yy:
        return 0
    else:
        # move right or down
        return count_paths(x+1,y, xx, yy) + count_paths(x, y-1, xx, yy)

print count_paths(0,2, 2,0)