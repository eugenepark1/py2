'''
Created on Oct 1, 2017

@author: eugene

given a collection of intervals, merge all overlapping intervals
given [1,3], [2,6], [8,10], [15,18]
return [1,6], [8,10], [15,18]
'''


def merge_intervals(intervals):
    
    merged_intervals = []
    curMin = None
    curMax = None
    for interval in intervals:
        tmpMin = interval[0]
        tmpMax = interval[1]
        
        if curMin is None:
            curMin = tmpMin
            curMax = tmpMax
        elif tmpMin < curMax:
            curMax = tmpMax
        else:
            merged_intervals.append([curMin, curMax])
            curMin = tmpMin
            curMax = tmpMax
        

    merged_intervals.append([curMin, curMax])

    return merged_intervals


intervals = [[1,3], [2,6], [8,10], [15,18]]

print merge_intervals(intervals)