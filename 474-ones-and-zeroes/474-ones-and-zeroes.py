from functools import lru_cache

class Solution:
    def get_freq(self, s):
        cc = {"0": 0, "1": 0}
        for c in s:
            cc[c] += 1
        return [cc["0"], cc["1"]]
    
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ln = len(strs)
        freq = [self.get_freq(s) for s in strs]
        inf = float('inf')
        
        @lru_cache(maxsize=None)
        def rec(i, c0, c1):
            if i == ln:
                return 0
            
            cc0, cc1 = freq[i]
            
            curr = rec(i + 1, c0, c1)
            if cc0 <= c0 and cc1 <= c1:
                curr = max(curr, rec(i + 1, c0 - cc0, c1 - cc1) + 1)
            
            return curr
        
        return rec(0, m, n)
