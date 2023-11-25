class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = sum(nums)

        result = [0] * n
        
        curr_sum = 0
        
        for i, x in enumerate(nums):
            before = x * i - curr_sum
            curr_sum += x
            after = s - curr_sum - x * (n - i - 1)
            result[i] = before + after

        return result
