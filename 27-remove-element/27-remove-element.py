class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        
        for n in nums:
            if (val == n):
                count += 1

        j = 0
        for i in range(len(nums)):
            # if (nums[i] == val):
            while (j < len(nums) and nums[j] == val):
                j += 1
            if (j == len(nums)):
                break
            # print(nums)
            nums[i] = nums[j]
            j += 1
        return len(nums) - count
    
