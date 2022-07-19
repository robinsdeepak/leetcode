from functools import lru_cache

MOD = 10 ** 9 + 7

class Solution:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        
        @lru_cache(None)
        def rec(sr, sc, mm):
            if sr < 0 or sr >= m or sc < 0 or sc >= n:
                return 1
            
            if mm == 0: return 0
            
            return  (
                rec(sr + 1, sc, mm - 1) + 
                rec(sr, sc + 1, mm - 1) + 
                rec(sr - 1, sc, mm - 1) + 
                rec(sr, sc - 1, mm - 1)
            ) % MOD
        
        return rec(startRow, startColumn, maxMove)
