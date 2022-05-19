from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = {}
        
        df = ((1, 0), (0, 1), (-1, 0), (0, -1))
        
        def valid(x, y):
            return (0 <= x < m) and (0 <= y < n)
        
        @lru_cache(maxsize=None)
        def dfs(x, y):
            if not valid(x, y):
                return 0
            
            curr = 0
            for dx, dy in df:
                x2, y2 = x + dx, y + dy
                if valid(x2, y2) and matrix[x][y] < matrix[x2][y2]:
                    curr = max(curr, dfs(x2, y2))
            return curr + 1
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        
        return ans
