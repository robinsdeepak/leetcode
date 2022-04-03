class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        p = n - 2
        
        while p >= 0 and nums[p] >= nums[p + 1]:
            p -= 1

        if p == -1:
            nums.reverse()
            return
        
        r = p + 1
        
        for i in range(r, n):
            if nums[p] < nums[i] < nums[r]:
                r = i
        
        nums[p], nums[r] = nums[r], nums[p]
        
        nums[p + 1:] = sorted(nums[p + 1:])
