'''
Created on Oct 3, 2018

@author: eugene
'''
def countSubstrings(s):
    if not s:
        return 0

    n = len(s)
    table = [[False for x in range(n)] for y in range(n)]
    count = 0

    # Every isolated char is a palindrome
    for i in range(n):
        table[i][i] = True
        count += 1

    # Check for a window of size 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            table[i][i+1] = True
            count += 1

    # Check windows of size 3 and more
    for k in range(3, n+1):
        for i in range(n-k+1):
            j = i+k-1
            if table[i+1][j-1] and s[i] == s[j]:
                table[i][j] = True
                count += 1

    return count

def countSubstrings_manachers(S):
    def manachers(S):
        A = '@#' + '#'.join(S) + '#$'
        Z = [0] * len(A)
        center = right = 0
        for i in xrange(1, len(A) - 1):
            if i < right:
                Z[i] = min(right - i, Z[2 * center - i])
            while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                Z[i] += 1
            if i + Z[i] > right:
                center, right = i, i + Z[i]
        return Z

    return sum((v+1)/2 for v in manachers(S))


def countSubstrings_expand_center(S):
    N = len(S)
    ans = 0
    for center in xrange(2*N - 1):
        left = center / 2
        right = left + center % 2
        while left >= 0 and right < N and S[left] == S[right]:
            ans += 1
            left -= 1
            right += 1
    return ans
    
print countSubstrings("aaa")