'''
Created on Oct 16, 2017

@author: eugenep

given a throughput (throughput meaning, how many jobs which can run in parallel, not a dispatch throughput)
to elaborate, even if you have a throughput of 1000 jobs/sec, if there are 10 cores, then obv not all 1000 jobs will run in parallel
in this problem, we will assume that there are enough resources to match throughput 

find the minimum throughput for minimum elapsed time
    implies in what order job needs to be dispatched - always sorted
'''
import random

# klibo@ontap
freqMap = {
    153: 1,
    31: 1,
    25: 1, 
    24: 1,
    17: 2,
    16: 1,
    15: 1,
    14: 1,
    13: 2,
    12: 4,
    11: 5,
    10: 2,
    9: 9,
    8: 13,
    7: 32,
    6: 41,
    5: 108,
    4: 254,
    3: 502,
    2: 1100,
    1: 790,
    0: 2099
    }

compile_times = []
for k,v in freqMap.iteritems():
    if k == 0:
        compile_times += [round(random.random(),4) for i in range(v)]
    else:
        compile_times += [k]*v
print compile_times

#compile_times = [5,1,1,1,1]
#compile_times.reverse()
tp = 48
max_parallel = 12*4

running = []
elapsed_time = 0
while True:
    
    # decr running jobs
    tmp_running = []
    for i in running:
        i = i-1
        if i > 0:
            tmp_running.append(i)
    running = tmp_running

    # dispatch jobs
    cnt = 0
    while True:
        if len(running) == max_parallel:
            break

        if len(compile_times) > 0:
            running.append( compile_times.pop(0) )
            cnt += 1
            if cnt == tp:
                break
        else:
            break

    elapsed_time += 1
    
    print "remaing jobs: %s" % compile_times
    print "running jobs: %s" % running
    print "elapsed time %s"  % elapsed_time

    if len(running) == 0:
        break

    

