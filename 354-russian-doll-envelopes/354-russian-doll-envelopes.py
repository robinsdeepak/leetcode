from functools import lru_cache

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        
        if n < 2: return n
        
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        dp = [1] * n
        size = 0        

        for envelope in envelopes:
            left, right = 0, size
            while left < right:
                mid = left + (right - left) // 2
                if dp[mid] < envelope[1]:
                    left = mid + 1
                else:
                    right = mid
            
            dp[left] = envelope[1]
            if left == size:
                size += 1
        
        return size
