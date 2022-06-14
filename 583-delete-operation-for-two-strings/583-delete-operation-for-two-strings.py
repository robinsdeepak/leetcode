from functools import lru_cache


class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        # return len(w1) + len(w2) - 2 * self.lcs_memo(w1, w2)
        # return len(w1) + len(w2) - 2 * self.lcs_dp(w1, w2)
        # return len(w1) + len(w2) - 2 * self.lcs_dp2(w1, w2)
        # return self.solution_rec(w1, w2)
        
        return self.solution_dp(w1, w2)
    
    def lcs_memo(self, w1, w2):
        
        @lru_cache(maxsize=None)
        def lcs(i, j):
            if i == -1 or j == -1:
                return 0
        
            if w1[i] == w2[j]:
                return 1 + lcs(i - 1, j - 1)

            return max(lcs(i - 1, j), lcs(i, j - 1))

        return lcs(len(w1) - 1, len(w2) - 1)

    def lcs_dp(self, w1, w2):
        
        n1, n2 = len(w1), len(w2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if w1[i - 1] == w2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n1][n2]

    def lcs_dp2(self, w1, w2):
        
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
    
    def solution_rec(self, w1, w2):
        
        @lru_cache(maxsize=None)
        def rec(i, j):
            if i == 0: return j
            if j == 0: return i
            
            if w1[i - 1] == w2[j - 1]:
                return rec(i - 1, j - 1)
            
            return min(rec(i - 1, j), rec(i, j - 1)) + 1
            
        return rec(len(w1), len(w2))

    def solution_dp(self, w1, w2):
        n1, n2 = len(w1), len(w2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif w1[i - 1] == w2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        
        return dp[n1][n2]
