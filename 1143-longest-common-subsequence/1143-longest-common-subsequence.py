from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        self.s1 = s1
        self.s2 = s2
        
        return self.rec(len(s1) - 1, len(s2) - 1)
        
    @lru_cache(maxsize=None)
    def rec(self, i1, i2):
        if i1 < 0 or i2 < 0:
            return 0

        if self.s1[i1] == self.s2[i2]:
            return 1 + self.rec(i1 - 1, i2 - 1)

        return max(self.rec(i1 - 1, i2), self.rec(i1, i2 - 1))

