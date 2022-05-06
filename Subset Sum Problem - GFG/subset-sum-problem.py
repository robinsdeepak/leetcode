#User function Template for python3

class Solution:
    def isSubsetSum (self, n, arr, sm):
        dp = {i: {} for i in range(n)}
        
        def rec(i, t):
            if t == 0: return True
            if i < 0 or t < 0: return False
            
            if dp[i].get(t) is not None:
                return dp[i][t]
            
            dp[i][t] = rec(i - 1, t - arr[i]) or rec(i - 1, t)
            
            return dp[i][t]
        
        return rec(n - 1, sm)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends