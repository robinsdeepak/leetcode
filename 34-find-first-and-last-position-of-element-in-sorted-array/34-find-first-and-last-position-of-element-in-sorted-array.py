class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
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

