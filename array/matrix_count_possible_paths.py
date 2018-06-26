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