class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        bins = {s[i - k : i] for i in range(k, len(s) + 1)}
        return len(bins) == 1 << k
