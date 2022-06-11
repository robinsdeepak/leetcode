class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        t = sum(nums) - x
        if t == 0: return n
        
        i, curr_sum, ans = 0, 0, n + 1
        
        for j in range(n):
            curr_sum += nums[j]
            while i <= j and curr_sum > t:
                curr_sum -= nums[i]
                i += 1
            
            if curr_sum == t:
                ans = min(ans, n - (j - i + 1))
        
        return ans if ans < n else -1
