class Solution:
    
    def __init__(self):
        self.ans = []
    
    def backtrack(self, x, k, n, path):
        
        if k == 0 and n == 0:
            self.ans.append(path.copy())
        
        if k <= 0 or n <= 0:
            return
        
        for i in range(x, 10):
            path.append(i)
            self.backtrack(i + 1, k - 1, n - i, path)
            path.pop()
            
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtrack(1, k, n, [])
        return self.ans

