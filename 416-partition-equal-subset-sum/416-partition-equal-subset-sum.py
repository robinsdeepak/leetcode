from functools import lru_cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm & 1: return False
        
        @lru_cache(maxsize=None)
        def solve(i, s):
            if i < 0: 
                return False
            
            if s == sm // 2:
                return True
            
            return solve(i - 1, s) or solve(i - 1, s + nums[i])
        
        return solve(len(nums) - 1, 0)
