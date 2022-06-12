class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        hset = set()
        
        i = 0
        curr, mx = 0, 0
        for j, x in enumerate(nums):
            
            while x in hset:
                hset.remove(nums[i])
                curr -= nums[i]
                i += 1
                
            hset.add(x)
            curr += x
            mx = max(mx, curr)
        
        return mx
