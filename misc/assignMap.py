'''
Created on Oct 16, 2017

@author: eugenep


given a list of jobs' expectued durs and q weight, distribute the jobs so that q's weight is the most balanced
most_balanced = diff amonst weights of Q's are minimal

queues = {
        q1: (weight1, num_of_workers1),
        ...
        qn: (weightn, num_of_workersn)
        }

where (1,1) == (8,8) as q_constant = weight/num_of_workers

jobs = (<cpus>, <time>)
where cpu > 1, reduces num_of_workes by <cpus>-1 until <time>


    now, if cpus is > 1, it will reduce the number of jobs which can be run on the node of the queue
    so this has to be taken into an account
'''

import random


def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/float(n) # in Python 2 use sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def stddev(data, ddof=0):
    """Calculates the population standard deviation
    by default; specify ddof=1 to compute the sample
    standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/(n-ddof)
    return pvar**0.5


times = []
queues = dict( zip( [i for i in range(12)], [(random.randint(0,12), 4) for i in range(12)]) )
print queues


jobs = [(random.randint(1,10), random.randint(1,10)) for i in range(10)]
def assign(jobs, queues):
    return

def calculate_stddev_balanceConstant(queues):
    '''
    lower the value the more balanced it is
    
    queues = {
        q1: (weight1, num_of_workers1),
        ...
        qn: (weightn, num_of_workersn)
    }
    
    balance_constant should be elapsed time
    
    '''
    q_constant = [ tup_v[0]/tup_v[1] for tup_v in queues.itervalues()]
    print q_constant
    return stddev(q_constant)
    
print calculate_stddev_balanceConstant(queues)