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