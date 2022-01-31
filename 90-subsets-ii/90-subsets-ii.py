class Solution:
    def __init__(self):
        self.ans = []
        
    def solve(self, nums, curr, start):
        self.ans.append(curr.copy())

        for i in range(start, len(nums)):
            if ((i == start) or (nums[i] != nums[i - 1])):
                curr.append(nums[i])
                self.solve(nums, curr, i + 1)
                curr.pop()
                
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.solve(nums, [], 0)
        return self.ans
