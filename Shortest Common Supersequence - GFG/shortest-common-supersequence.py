#User function Template for python3

class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        return m + n - self.lcs(X, Y)
    
    def lcs(self, w1, w2):
        n1, n2 = len(w1), len(w2)
        dp = [0] * (n2 + 1)
        
        for i in range(1, n1 + 1):
            temp = [0] * (n2 + 1)
            for j in range(1, n2 + 1):
                if w1[i - 1] == w2[j - 1]:
                    temp[j] = dp[j - 1] + 1
                else:
                    temp[j] = max(dp[j], temp[j - 1])
            dp = temp
                
        return dp[n2]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
        
# } Driver Code Ends