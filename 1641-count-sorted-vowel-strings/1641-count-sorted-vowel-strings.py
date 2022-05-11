from functools import lru_cache

class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def rec(c, f):
            if c == 4: return 1
            if f == 1: return 5 - c
            
            res = 0
            for ff in range(f + 1):
                res += rec(c + 1, f - ff)
            return res
        
        return rec(0, n)
