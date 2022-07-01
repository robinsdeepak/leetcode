class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        m = nums[n // 2]
        
        return sum(abs(m - x) for x in nums)
