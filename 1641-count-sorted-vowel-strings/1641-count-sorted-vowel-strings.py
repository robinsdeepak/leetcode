from functools import lru_cache

class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def rec(c, f):
            if f == 0:
                return 1
            
            if c == 5:
                return 0
            
            res = 0
            for ff in range(f + 1):
                res += rec(c + 1, f - ff)
            return res
        
        return rec(0, n)
