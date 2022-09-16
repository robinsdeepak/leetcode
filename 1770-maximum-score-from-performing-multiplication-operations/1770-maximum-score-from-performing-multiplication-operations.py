from functools import lru_cache

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        return self.solution_2(nums, multipliers)
        
    
    def solution_1(self, nums, multipliers):
        n = len(nums)
        m = len(multipliers)
        
        dp = {}
        
        def rec(i, j):
            if i == m:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            dp[(i, j)] = max(
                rec(i + 1, j + 1) + (nums[j] * multipliers[i]),
                rec(i + 1, j) + (nums[(n - 1) - (i - j)] * multipliers[i])
            )
            return dp[(i, j)]
        
        return rec(0, 0)

    def solution_2(self, nums, multipliers):
        n = len(nums)
        m = len(multipliers)
        
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for j in range(i, -1, -1):
                dp[i][j] = max(
                    dp[i + 1][j + 1] + (nums[j] * multipliers[i]),
                    dp[i + 1][j] + (nums[(n - 1) - (i - j)] * multipliers[i])
                )
        return dp[0][0]
