class Solution:

#     def maxProduct(self, nums: List[int]) -> int:
#
#         prefix, suffix, res = 0, 0, float('-inf')
#         for i in range(len(nums)):
#             prefix = (prefix or 1) * nums[i]
#             suffix = (suffix or 1) * nums[~i]
#             res = max(res, prefix, suffix)
#         return res
    
    def maxProduct(self, nums):
        curr_min = curr_max = 1
        ans = float('-inf')
        
        for x in nums:
            temp = (curr_min * x, curr_max * x, x)
            curr_max = max(temp)
            curr_min = min(temp)
            ans = max(curr_max, ans)
        
        return ans
