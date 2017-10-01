'''
Created on Aug 31, 2017

@author: eugene

Dynamic Programming
Given a matrix of positive integers,
reach from the top left corner to bottom right 
in minimum cost
You can only go one square right, down, or diagonally right-down
The cost is the sum of squares you've covered
i.e
4 5 6
1 2 3
0 1 2
ans: 8 (4+1+0+1+2)
'''

def legal_grid(x, y):
    if x < end_x and y < end_y and x >= 0 and y >= 0:
        return True
    return False

def sumPath(x, y, depth):
    global board

    if x == end_x-1 and y == end_y-1:
        print "we are at the end: 2,2"
        return board[x][y]

    elif not legal_grid(x, y):
        return None

    print "\t"*depth  + "current: %s,%s" % (x,y)

    bottom = sumPath(x, y+1, depth+1)
    right = sumPath(x+1, y , depth+1)
    botrgt = sumPath(x+1, y+1, depth+1)

    print "\t"*depth  + "bottom (%s,%s): %s" % (x, y+1, bottom)
    print "\t"*depth  + "right (%s,%s): %s" % (x+1,y, right)
    print "\t"*depth  + "bottom-right (%s,%s): %s" % (x+1,y+1,botrgt)

    # there will be never a case where all three possible steps are invalid
    min_weight = -1
    if bottom is not None:
        min_weight = bottom

    if right is not None:
        if min_weight < 0:
            min_weight = right
        elif right < min_weight:
            min_weight = right

    if botrgt is not None:
        if min_weight < 0:
            min_weight = botrgt
        elif botrgt < min_weight:
            min_weight = botrgt

    if min_weight > 0:
        return board[x][y] + min_weight
    else:
        return board[x][y]

### START
#board = [ [None]*10 for _ in range(10) ]
board = [ [4,1,0], [5,2,1], [6,3,2] ]
print board

end_x = len(board)
end_y = len(board[-1])
print "Board is %s x %s" % (end_x, end_y)

print "ans: %s" % sumPath(0, 0, 1)