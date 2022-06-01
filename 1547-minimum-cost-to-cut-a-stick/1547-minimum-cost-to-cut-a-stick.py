from functools import lru_cache

class Solution:
    
    
    def minCost(self, n: int, cuts: List[int]) -> int:
        return self.solution_2(n, cuts)

    def solution_2(self, n, cuts):
        c = len(cuts)
        cuts = [0] + sorted(cuts) + [n]
        
        dp = [[0] * (c + 2) for _ in range(c + 2)]
        
        for i in range(c, 0, -1):
            for j in range(1, c + 1):
                if i > j: continue
                    
                mini = float('inf')

                for x in range(i, j + 1):
                    curr = dp[i][x - 1] + dp[x + 1][j] + cuts[j + 1] - cuts[i - 1]

                    mini = min(curr, mini)

                dp[i][j] = mini
                    
        return dp[1][c]
        
    def solution_1(self, n, cuts):
        c = len(cuts)
        cuts = [0] + sorted(cuts) + [n]
        
        @lru_cache(maxsize=None)
        def solve(i, j):
            if i > j: return 0
            
            ans = float('inf')
            
            for x in range(i, j + 1):
                curr = solve(i, x - 1) + \
                       solve(x + 1, j) + \
                       cuts[j + 1] - cuts[i - 1]
                
                ans = min(curr, ans)
            
            return ans
        
        return solve(1, c - 2)