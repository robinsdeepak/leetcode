class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        c = 0
        
        for i in range(1, n):
            
            if nums[i - 1] > nums[i]:
                if c == 1: return False
                
                c += 1
                
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        
        return True
