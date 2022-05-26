from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        self.s1 = s1
        self.s2 = s2
        
        # return self.rec(len(s1) - 1, len(s2) - 1)
        return self.tab()
    
    def tab(self):
        m = len(self.s1)
        n = len(self.s2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.s1[i - 1] == self.s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # for r in dp: print(r)
            
        return dp[m][n]
        
    @lru_cache(maxsize=None)
    def rec(self, i1, i2):
        if i1 < 0 or i2 < 0:
            return 0

        if self.s1[i1] == self.s2[i2]:
            return 1 + self.rec(i1 - 1, i2 - 1)

        return max(self.rec(i1 - 1, i2), self.rec(i1, i2 - 1))

