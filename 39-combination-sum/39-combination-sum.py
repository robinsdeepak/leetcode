class Solution:
    def __init__(self):
        self.ans = []
    
    def solve(self, candidates, target, curr, curr_sum, i):
        if (curr_sum == target):
            self.ans.append(curr.copy())
            return
            
        if (i == len(candidates)):
            return
        self.solve(candidates, target, curr, curr_sum, i + 1)
        
        count = 0
        while ((curr_sum + candidates[i]) <= target):
            count += 1
            curr.append(candidates[i])
            curr_sum += candidates[i]
            self.solve(candidates, target, curr, curr_sum, i + 1)
            
        for _ in range(count):
            curr.pop()
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.solve(candidates, target, [], 0, 0)
        return self.ans
