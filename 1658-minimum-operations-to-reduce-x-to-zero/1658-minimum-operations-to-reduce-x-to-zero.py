from functools import lru_cache


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        t = sum(nums) - x
        
        if t == 0: return n
        
        m = {0: -1}
        l = -1
        s = 0
        for i in range(n):
            s += nums[i]
            if s - t in m:
                l = max(l, i - m[s - t])
            
            m[s] = i
        
        return -1 if l == -1 else n - l
    