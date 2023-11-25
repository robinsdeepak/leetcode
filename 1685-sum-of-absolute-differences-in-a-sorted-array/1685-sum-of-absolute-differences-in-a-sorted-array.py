class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = sum(nums)
        result = [0] * n
        result[0] = s - n * (nums[0])
        for i in range(1, n):
            result[i] = result[i - 1] + (i + i - n) * (nums[i] - nums[i - 1])
        return result
