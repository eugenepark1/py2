'''
Created on Aug 12, 2018

@author: eugene

    1 1 1 1
    0 1 1 1
    0 1 0 1
    1 1 9 1
    0 0 1 1
    
find min Path to '9' where only valid paths taken should consists of '1's and only can go up, down, left, right
'''


lot = [
        [1, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 1, 0, 1],
        [1, 1, 9, 1],
        [0, 0, 1, 1]
    ]

def traverse(x, y, max_x, max_y, visited, lot):
    
    visited.append((x,y))
    print "(%s, %s)" % (x,y)
    print max_x
    print max_y
    
    if lot[x][y] == 9:
        return 0
    elif lot[x][y] == 0:
        return 0
    else:
        valid_values = [0]
        if y > 0 and (x,y-1) not in visited:
            up = traverse(x, y-1, max_x, max_y, visited, lot)
        
        if y < max_y and (x, y+1) not in visited:
            down = traverse(x, y+1, max_x, max_y, visited, lot)
        
        if x > 0 and (x-1,y) not in visited:
            left = traverse(x-1, y, max_x, max_y, visited, lot)
        
        if x < max_x and (x+1,y) not in visited:
            right = traverse(x+1, y, max_x, max_y, visited, lot)
    
    return min(valid_values) + 1


for k,i in enumerate(lot):
    print "%s: %s" % (k,i)

#print traverse(0, 0, len(lot[0]), len(lot), [], lot)