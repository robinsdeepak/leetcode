class Solution:
    def __init__(self):
        self.ans = []
    
    def solve(self, target, c, curr):
        # print(c, curr, target)

        if (target == 0):
            self.ans.append(curr)
            return
        
        if (target < 0):
            return

        for i in range(len(c)):
            if (i == 0 or c[i] != c[i - 1]):
                self.solve(target - c[i], c[i+1:], curr + [c[i]])
        
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.solve(target, candidates, [])
        return self.ans
