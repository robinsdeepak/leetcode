#User function Template for python3
from functools import lru_cache
import sys
sys.setrecursionlimit(1000000)

class Solution:
	def maxSumIS(self, arr, n):
	   # @lru_cache(maxsize=None)
    #     def rec(i, l):
    #         if i < 0: return 0
    #         ans = rec(i - 1, l)
    #         if l == -1 or arr[i] < arr[l]:
    #             ans = max(ans, rec(i - 1, i) + arr[i])
    #         return ans
    #     return rec(n - 1, -1)
    
        dp = arr.copy()
        ans = arr[0]
        for i in range(n):
            for j in range(i+1):
                if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
                    dp[i] = dp[j] + arr[i]
                    
                    if ans < dp[i]: ans = dp[i]
        
        return ans
    
    
    
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends