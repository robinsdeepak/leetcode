class Solution:
    def solve(self, nums, ans, curr, idx):
        if (idx == len(nums)):
            ans.append(curr)
            return
        
        self.solve(nums, ans, curr + [nums[idx]], idx + 1)
        self.solve(nums, ans, curr, idx + 1)
        
    
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.solve(nums, ans, [], 0)
        return ans
