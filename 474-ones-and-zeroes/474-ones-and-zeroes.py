from functools import lru_cache

class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
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
