class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1: return 1
        
        prev = nums[1] - nums[0]
        
        count = 1 if prev == 0 else 2
        
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            
            if (diff < 0 and prev >= 0) or (diff > 0 and prev <= 0):
                count += 1
                prev = diff

        return count
