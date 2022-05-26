from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        
        @lru_cache(maxsize=None)
        def rec(i1, i2):
            if i1 < 0 or i2 < 0:
                return 0
            
            if s1[i1] == s2[i2]:
                return 1 + rec(i1 - 1, i2 - 1)
            
            return max(rec(i1 - 1, i2), rec(i1, i2 - 1))
        
        return rec(len(s1) - 1, len(s2) - 1)
