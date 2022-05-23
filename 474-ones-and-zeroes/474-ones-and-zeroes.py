from functools import lru_cache

class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.iterative(strs, m, n)
    
    def iterative(self, strs, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            c0 = s.count("0")
            c1 = len(s) - c0
            
            for i in range(m, c0 - 1, -1):
                for j in range(n, c1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - c0][j - c1] + 1)
            
        return dp[m][n]
    
    def recursive(self, strs, m, n):
        ln = len(strs)
        inf = float('inf')
        
        @lru_cache(maxsize=None)
        def rec(i, c0, c1):
            if c0 < 0 or c1 < 0: return -inf
            if i == ln: return 0
            
            cc0 = strs[i].count("0")
            cc1 = len(strs[i]) - cc0
            
            return max(rec(i + 1, c0, c1), rec(i + 1, c0 - cc0, c1 - cc1) + 1)
            
        return rec(0, m, n)
