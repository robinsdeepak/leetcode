class Solution:
    def __init__(self):
        self.ans = []
    
    def solve(self, candidates, target, curr):
        if (target == 0):
            self.ans.append(curr.copy())
            return
        if (target < 0):
            return 
        
        for i in range(len(candidates)):
            self.solve(candidates[i:], target-candidates[i], curr+[candidates[i]])
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.solve(candidates, target, [])
        return self.ans
