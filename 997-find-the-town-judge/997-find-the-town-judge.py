class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        g = [[0] * n for _ in range(n)]
        
        for i, j in trust:
            g[i - 1][j - 1] = 1
                
        
        for i in range(n):
            if sum(g[i]) == 0:
                s = sum(map(lambda x: x[i], g))
                if s == n - 1:
                    return i + 1
            
        return -1
