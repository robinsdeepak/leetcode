from functools import lru_cache


class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        return len(w1) + len(w2) - 2 * self.lcs_rec(w1, w2)
    
    def lcs_rec(self, w1, w2):
        
        @lru_cache(maxsize=None)
        def lcs(i, j):
            if i == -1 or j == -1:
                return 0
        
            if w1[i] == w2[j]:
                return 1 + lcs(i - 1, j - 1)

            return max(lcs(i - 1, j), lcs(i, j - 1))

        return lcs(len(w1) - 1, len(w2) - 1)
