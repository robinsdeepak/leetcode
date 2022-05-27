class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.lcs(s, s[::-1])
        
    def lcs(self, w1, w2):
        n1, n2 = len(w1), len(w2)
        # memo = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        dp = [0] * (n2 + 1)
        
        for i in range(1, n1 + 1):
            temp = [0] * (n2 + 1)
            for j in range(1, n2 + 1):
                if w1[i - 1] == w2[j - 1]:
                    # memo[i][j] = memo[i - 1][j - 1] + 1
                    temp[j] = dp[j - 1] + 1
                else:
                    # memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
                    temp[j] = max(dp[j], temp[j - 1])
            dp = temp
                
        return dp[n2]
