class Solution:
    
    def solve(self, i, k, n, curr, ans):
        if (len(curr) == k):
            ans.append(curr)
            return
        
        if (i > n):
            return
        
        self.solve(i+1, k, n, curr, ans)
        self.solve(i+1, k, n, [i] + curr, ans)
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.solve(1, k, n, [], ans)
        return ans
