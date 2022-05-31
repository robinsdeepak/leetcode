class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if (len(s) - k + 1) < (1 << k):
            return False
        
        bins = {s[i - k : i] for i in range(k, len(s) + 1)}
        return len(bins) == 1 << k
