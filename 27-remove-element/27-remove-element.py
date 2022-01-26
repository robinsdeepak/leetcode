class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        
        j = 0
        for i in range(len(nums)):
            while (j < len(nums) and nums[j] == val):
                j += 1
                count += 1
            if (j == len(nums)):
                break
            nums[i] = nums[j]
            j += 1
        return len(nums) - count

