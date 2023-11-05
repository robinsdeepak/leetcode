class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        diff = 0
        n = len(nums)
        for i in range(1, n):
            curr_diff = nums[i] - nums[i - 1]
            if diff * curr_diff < 0:
                return False
            if diff == 0 and curr_diff != 0:
                diff = curr_diff
        return True

