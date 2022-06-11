from functools import lru_cache


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        
        if nums[0] == x: 
            return 1
        
        ans = n + 1
        curr_sum = nums[0]
        t = sum(nums) - x
        i = 0
        
        if curr_sum == t:
            ans = n - 1
        
        for j in range(1, n):
            curr_sum += nums[j]
            while i <= j and curr_sum > t:
                curr_sum -= nums[i]
                i += 1
            
            if curr_sum == t:
                ans = min(ans, n - (j - i + 1))
        
        return ans if ans < n + 1 else -1
