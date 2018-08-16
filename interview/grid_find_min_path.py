'''
Created on Aug 12, 2018

@author: eugene

    1 1 1 1
    0 1 1 1
    0 1 0 1
    1 1 9 1
    0 0 1 1
    
find min Path to '9' where only valid paths taken should consists of '1's and only can go up, down, left, right
x = cols
y = rows
'''


lot = [
        [1, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 1, 0, 1],
        [1, 1, 9, 1],
        [0, 0, 1, 1]
    ]

def traverse(x, y, max_x, max_y, visited, tab_cnt, action, lot):
    tab_cnt =  tab_cnt + 1
    
    visited.append((x,y))
    
    tab_str = "\t".join(['' for i in range(tab_cnt)])
    print "%s(%s, %s) %s" % (tab_str, x, y, action)
    #print "%smax_x (cols) %s" % (tab_str,max_x)
    #print "%smax_y (rows) %s" % (tab_str,max_y)
    
    if lot[x][y] == 9:
        print "%sfound 9" % tab_str
        return 0
    elif lot[x][y] == 0:
        return 0
    else:
        valid_values = [0]
        
        print "%s%s" % (tab_str, visited)
        if y > 0 and (x,y-1) not in visited:
            print "%sgoing up" % tab_str
            up = traverse(x, y-1, max_x, max_y, visited, tab_cnt, "up", lot)
            if up > 0:
                valid_values.append(up)
        
        if y < max_y and (x, y+1) not in visited:
            print "%sgoing down" % tab_str
            down = traverse(x, y+1, max_x, max_y, visited, tab_cnt, "down", lot)
            if down > 0:
                valid_values.append(down)
        
        if x > 0 and (x-1,y) not in visited:
            print "%sgoing left" % tab_str
            left = traverse(x-1, y, max_x, max_y, visited, tab_cnt, "left", lot)
            if left > 0:
                valid_values.append(left)
        
        print "%s%s" % (tab_str, visited)
        if x < max_x-1 and (x+1,y) not in visited:
            print "%sgoing right" % tab_str
            right = traverse(x+1, y, max_x, max_y, visited, tab_cnt, "right", lot)
            if right > 0:
                valid_values.append(right)
    
        print "%s%s" % (tab_str, valid_values)
        return max(valid_values) + 1


for k,i in enumerate(lot):
    print "%s: %s" % (k,i)

print traverse(0, 0, len(lot[0])-2, len(lot)-2, [], 0, "root", lot)