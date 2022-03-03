class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        
        last = 0
        total = 0
        for i in range(2, n):
            total += last
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                last += 1
            else:
                last = 0
        
        return total + last

