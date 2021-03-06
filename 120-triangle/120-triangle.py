from functools import lru_cache

INF = float('inf')

class Solution:
    def minimumTotal(self, tr: List[List[int]]) -> int:
        return self.solution_4(tr)
    
    def solution_1(self, tr):
        n = len(tr)
        
        @lru_cache(maxsize=None)
        def rec(r, c):
            if r == n: return 0
            if c == tr[r]: return INF
            
            return tr[r][c] + min(rec(r + 1, c), rec(r + 1, c + 1))
        
        return rec(0, 0)

    def solution_2(self, tr):
        n = len(tr)
        
        dp = [[INF] * (n + 1) for _ in range(n + 1)]
        dp[n] = [0] * (n + 1)
        
        for r in range(n - 1, -1, -1):
            for c in range(r + 1):
                dp[r][c] = tr[r][c] + min(dp[r + 1][c], dp[r + 1][c + 1])
                
        return dp[0][0]

    def solution_3(self, tr):
        n = len(tr)
        
        dp = [0] * (n + 1)
        
        for r in range(n - 1, -1, -1):
            temp = [INF] * (r + 1)
            for c in range(r + 1):
                temp[c] = tr[r][c] + min(dp[c], dp[c + 1])
            dp = temp
        
        return dp[0]
    
    def solution_4(self, tr):
        n = len(tr)
        
        for i in range(1, n):
            for j in range(i + 1):
                tr[i][j] = tr[i][j] + min(tr[i - 1][max(0, j - 1)], tr[i - 1][min(i - 1, j)])
        
        return min(tr[n - 1])
