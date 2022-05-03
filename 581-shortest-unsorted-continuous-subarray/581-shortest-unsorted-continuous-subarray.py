class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        nums2 = sorted(nums)
        for i in range(n-1):
            if nums[i] != nums2[i]:
                break
        else:
            return 0
        
        s = i
        e = i + 1
        
        for i in range(s, n):
            if nums[i] != nums2[i]:
                e = i
        
        return e - s + 1
