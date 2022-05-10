class Solution:
    
    def __init__(self):
        self.ans = []
    
    def backtrack(self, nums, k, n, path):
        
        if k == 0 and n == 0:
            self.ans.append(path.copy())
        
        if k < 0 or n < 0:
            return
        
        for i in range(len(nums)):
            path.append(nums[i])
            self.backtrack(nums[i+1:], k - 1, n - nums[i], path)
            path.pop()
            
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtrack(list(range(1, 10)), k, n, [])
        return self.ans

