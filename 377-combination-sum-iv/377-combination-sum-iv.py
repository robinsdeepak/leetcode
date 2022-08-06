class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        
        def rec(t):
            if t == 0: return 1
            if t in dp: return dp[t]
            ans = 0
            for x in nums:
                if (x <= t):
                    ans += rec(t - x)
            dp[t] = ans
            return ans
        
        return rec(target)

