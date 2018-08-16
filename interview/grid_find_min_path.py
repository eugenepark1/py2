import copy
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
    
    tmp_visited = copy.deepcopy(visited)
    visited.append((x,y))
    
    tab_str = "\t".join(['' for i in range(tab_cnt)])
    print "%s(%s, %s) %s" % (tab_str, x, y, action)
    #print "%smax_x (cols) %s" % (tab_str,max_x)
    #print "%smax_y (rows) %s" % (tab_str,max_y)
    
    cur_value = lot[x][y]
    if lot[x][y] == 9:
        print "%sfound 9" % tab_str
        return 1
    elif lot[x][y] == 0:
        print "%sfound 0" % tab_str
        return -1
    else:
        valid_values = [0]
        
        print "%s%s" % (tab_str, tmp_visited)
        if y > 0 and (x,y-1) not in tmp_visited:
            print "%sgoing left" % tab_str
            up = traverse(x, y-1, max_x, max_y, visited, tab_cnt, "left", lot)
            if up > 0:
                valid_values.append(up)
        else:
            print "%snot going left %s %s" % (tab_str, y, (x,y-1))
        
        if y < max_y and (x, y+1) not in tmp_visited:
            print "%sgoing right" % tab_str
            down = traverse(x, y+1, max_x, max_y, visited, tab_cnt, "right", lot)
            if down > 0:
                valid_values.append(down)
        
        if x > 0 and (x-1,y) not in tmp_visited:
            print "%sgoing up" % tab_str
            left = traverse(x-1, y, max_x, max_y, visited, tab_cnt, "up", lot)
            if left > 0:
                valid_values.append(left)
        
        print "%s%s" % (tab_str, tmp_visited)
        if x < max_x and (x+1,y) not in tmp_visited:
            print "%sgoing down" % tab_str
            right = traverse(x+1, y, max_x, max_y, visited, tab_cnt, "down", lot)
            if right > 0:
                valid_values.append(right)
        else:
            print "%snot going down %s %s %s" % (tab_str, x, max_x, (x+1,y))
    
        print "%svalid values: %s" % (tab_str, valid_values)
        return max(valid_values) + 1


for k,i in enumerate(lot):
    print "%s: %s" % (k,i)

print traverse(0, 0, len(lot)-1, len(lot[0])-1, [], 0, "root", lot)