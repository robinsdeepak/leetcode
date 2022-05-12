#User function Template for python3

from functools import lru_cache

class Solution:
    def count(self, s, m, n): 
        
        @lru_cache(maxsize=None)
        def solve(i, curr):
            if curr == 0: return 1
            if curr < 0 or i < 0: return 0
            
            res = solve(i - 1, curr)
            while curr - s[i] >= 0:
                curr -= s[i]
                res += solve(i - 1, curr)
            
            return res
        
        return solve(m-1, n)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends