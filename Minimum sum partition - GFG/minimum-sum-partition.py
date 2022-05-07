#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
        sm = sum(arr)

        dp = {}
        
        def rec(i, s):
            if i < 0: 
                return abs(2 * s - sm)
            
            if (i, s) in dp: return dp[(i, s)]
            
            dp[(i, s)] = min(
                rec(i - 1, s + arr[i]), 
                rec(i - 1, s))
                
            return dp[(i, s)]
            
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