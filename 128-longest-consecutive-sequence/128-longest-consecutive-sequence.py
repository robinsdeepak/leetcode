class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0: return 0
        
        s = set(nums)
        ans = 1
        
        
        for x in s:
            
            if x - 1 not in s:
                curr = 1
                
                while x + 1 in s:
                    curr += 1
                    x += 1
                
                ans = max(curr, ans)
        
        return ans
