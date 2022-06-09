class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        n = len(nums)
        i = 0
        j = n - 1
        
        while i < j:
            s = nums[i] + nums[j]
            if s == t:
                return [i + 1, j + 1]
            elif s < t:
                i += 1
            else:
                j -= 1
            
        return [-1, -1]
