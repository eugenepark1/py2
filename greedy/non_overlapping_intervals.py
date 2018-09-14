'''
Created on Oct 9, 2017

@author: eugene

given a collection of intervals, find the min number of intervals you need to remove to make the rest of the interval non-overlapping
[ [1,2], [2,3], [3,4], [1,3] ]
output 1  [1,3] should be removed

classic greedy problem : interval scheduling


'''


intervals = [(1,2), (2,3), (3,4), (1,3)]
def nonoverlap(intervals):
    '''
    overlapping:
        s is between (s,e)  (1,2) (1,3) overlap  (1,2) (2,3) not overlap  
        e is between (s,e)  (1,3) (2,3) overlap  (1,3) (3,5) not overlap
        
    if cur_intv nooverlapping in tmp_intvs:
        add to tmp_intvs
        

    1,2 1,3   same same (s)
    '''
    
    tmp_intvs = []
    for cur_intv in intervals:
        c_start, c_end = cur_intv
        
        overlap = False
        for tmp_intv in tmp_intvs:
            t_start, t_end = tmp_intv
            if (c_start >= t_start and c_start < t_end) or (c_end > t_start and c_end <= t_end):
                overlap = True
                break
        if not overlap:
            tmp_intvs.append(cur_intv)
        
        
    return (len(intervals) - len(tmp_intvs), tmp_intvs)


print nonoverlap(intervals)