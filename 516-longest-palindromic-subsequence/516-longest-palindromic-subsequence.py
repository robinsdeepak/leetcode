from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.solution_2(s)
    
    def solution_2(self, s):
        # recursive and memoization
        
        @lru_cache(maxsize=None)
        def rec(i, j):
            if i == j: return 1
            if i > j: return 0

            if s[i] == s[j]:
                return 2 + rec(i + 1, j - 1)
            else:
                return max(rec(i + 1, j), rec(i, j - 1))
            
        return rec(0, len(s) - 1)
    
    def solution_1(self, s):
        # lcs and dp
        return self.lcs(s, s[::-1])
    
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
