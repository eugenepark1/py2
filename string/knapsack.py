'''
Created on Jun 29, 2018

@author: eugenep

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
'''

def knapsack(W, wt, val, n):
    dp = [[0 for i in range(W+1)]for j in range(n+1)]

    for i in range(1,n+1):
        for w in range(1,W+1):
            if(wt[i-1]<=w):
                dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][w]


#A naive recursive implementation of 0-1 Knapsack Problem
# Returns the maximum value that can be put in a knapsack of capacity W
# this is O(2^n) as the items are evaluated twice
# however, Like other typical Dynamic Programming(DP) problems, recomputations of same subproblems can be avoided by constructing a temporary array K[][] in bottom up manner. 
def knapSack(W , wt , val , n):
 
    # Base Case
    if n == 0 or W == 0 :
        return 0
 
    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W , wt , val , n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1),
                   knapSack(W , wt , val , n-1))
 
#Time Complexity: O(nW) where n is the number of items and W is the capacity of knapsack.
# build K(n, W)
def knapSack_efficient(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
 
 
# To test above function
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print knapSack(W , wt , val , n)