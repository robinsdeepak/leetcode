class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix, res = 0, 0, float('-inf')
        
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            res = max(res, prefix, suffix)
        return res
        