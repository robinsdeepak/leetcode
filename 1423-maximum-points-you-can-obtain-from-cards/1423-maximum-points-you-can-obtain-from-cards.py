class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        
        n = len(cp)
        t = sum(cp)

        if n == k:
            return t
        
        r = n - k
        mn = t
        s = 0
        
        for i in range(r - 1):
            s += cp[i]
        
        for i in range(r- 1, n):
            s += cp[i]            
            mn = min(mn, s)
            s -= cp[i - r + 1]
        
        return t - mn
