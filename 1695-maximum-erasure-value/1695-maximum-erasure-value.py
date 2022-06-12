class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
                
        found = [False] * 10001
        
        curr, mx = 0, 0
        
        i = 0

        for x in nums:
            
            while found[x]:
                found[nums[i]] = False
                curr -= nums[i]
                i += 1
                
            found[x] = True
            curr += x
            
            if curr > mx: mx = curr
        
        return mx
