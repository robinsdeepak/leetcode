#User function Template for python3
from functools import lru_cache

class Solution:
    def matrixMultiplication(self, n, arr):
        
        @lru_cache(None)
        def solve(s, e):
            # print(s, e)
            if s == e:
                return 0
            
            if s + 1 == e:
                return arr[s - 1] * arr[s] * arr[s + 1]
            
            ans = float('inf')
            
            for m in range(s, e):
                curr = solve(s, m) + solve(m + 1, e) + arr[s - 1] * arr[m] * arr[e]
                # print(s, m, e, curr)
                ans = min(ans, curr)
            
            return ans
            
        return solve(1, n - 1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends