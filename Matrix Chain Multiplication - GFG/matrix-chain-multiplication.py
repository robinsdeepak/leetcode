#User function Template for python3
from functools import lru_cache

class Solution:
    def matrixMultiplication(self, n, arr):
        return self.solution_1(n, arr)
        
    def solution_1(self, n, arr):
        @lru_cache(None)
        def solve(s, e):
            if s == e:
                return 0
            
            ans = float('inf')
            
            for m in range(s, e):
                left = solve(s, m)
                right = solve(m + 1, e)
                merge = arr[s - 1] * arr[m] * arr[e]
                curr = left + right + merge
                
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