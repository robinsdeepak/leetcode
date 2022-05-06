#User function Template for python3
from functools import lru_cache

class Solution:
	def minDifference(self, arr, n):
        sm = sum(arr)

        @lru_cache(maxsize=None)
        def rec(i, s):
            
            if i < 0: 
                return abs(2 * s - sm)
            
            return min(
                rec(i - 1, s + arr[i]), 
                rec(i - 1, s)
            )
            
        return rec(n - 1, 0)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends