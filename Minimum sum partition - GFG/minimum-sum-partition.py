#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
        sm = sum(arr)
        ans = sm
        dp = {i: {} for i in range(n)}
        
        def rec(i, fs):
            if i == n: return abs(2 * fs - sm)
            
            if dp[i].get(fs) is not None:
                return dp[i][fs]
            
            dp[i][fs] = min(rec(i + 1, fs + arr[i]), rec(i + 1, fs))
            
            return dp[i][fs]
            
        return rec(0, 0)
        


    def isSubsetSum(self, n, arr, sm):
        dp = {i: {} for i in range(n)}
        
        def rec(i, t):
            if t == 0: return True
            if i == 0: return arr[0] == t
            
            if dp[i].get(t) is not None:
                return dp[i][t]
            
            dp[i][t] = rec(i - 1, t - arr[i]) or rec(i - 1, t)
            
            return dp[i][t]
        
        return rec(n - 1, sm)

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