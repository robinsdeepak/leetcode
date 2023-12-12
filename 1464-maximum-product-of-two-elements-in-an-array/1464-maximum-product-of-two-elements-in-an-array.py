class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = nums[0], nums[1]
        a, b = max(a, b), min(a, b)
        
        for x in nums[2:]:
            if x > a:
                b = a
                a = x
            elif x > b:
                b = x
        return (b - 1) * (a - 1)
