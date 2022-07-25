import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.solution_2(nums, target)    
    
    def solution_2(self, nums, target):
        s = bisect.bisect_left(nums, target)
        
        if s == len(nums) or nums[s] != target:
            return [-1, -1]
        
        e = bisect.bisect_right(nums, target) - 1
        
        return [s, e]
    
        
    def solution_1(self, nums, target):
        n = len(nums)
                
        i, j = 0, n - 1
        
        ans = [-1, -1]
        
        while i <= j:
            m = (i + j) // 2
            
            if nums[m] == target:
                if m == 0 or nums[m - 1] < target:
                    ans[0] = m
                    break
                else:
                    j = m - 1
            
            elif nums[m] > target:
                j = m - 1
            
            else:
                i = m + 1
        
        if ans[0] == -1:
            return ans
        
        i, j = ans[0], n - 1
        
        while i <= j:
            m = (i + j) // 2
            
            if nums[m] == target:
                if m == n - 1 or nums[m + 1] > target:
                    ans[1] = m
                    break
                else:
                    i = m + 1
            elif nums[m] > target:
                j = m - 1
            
            else:
                i = m + 1
        
        return ans

