class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        major = 0
        
        for x in nums:
            if count == 0:
                major = x
            if major == x:
                count += 1
            else:
                count -= 1
        return major

