from functools import lru_cache

class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def rec(c, f):
            if c == 4 or f == 0: 
                return 1
            
            return sum(rec(c + 1, f - ff) for ff in range(f + 1))
                    
        return rec(0, n)
