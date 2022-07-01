class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        curr = 0
        ans = float('inf')
        nums.sort()
        
        for i in range(n):
            curr += nums[i]
            c1 = nums[i] * (i + 1) - curr
            c2 = (total - curr) - nums[i] * (n - i - 1)
            # print(ans, c1, c2)
            ans = min(ans, c1 + c2)
        
        return ans
