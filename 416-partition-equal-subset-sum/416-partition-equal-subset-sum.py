from functools import lru_cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return self.solution_3(nums)
    
    def solution_2(self, nums):
        # tabulation
        sm = sum(nums)
        half = sm // 2
        
        
    def solution_3(self, nums):
        total_sum = sum(nums)
        if total_sum & 1: return False
        half_sum, dp = total_sum // 2, 1
        for num in nums:
            dp |= dp << num
        return dp & 1 << half_sum
        
        
        
    def solution_1(self, nums):
        # memoization
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
