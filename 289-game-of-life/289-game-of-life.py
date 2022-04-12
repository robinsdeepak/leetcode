class Solution:
    def gameOfLife(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m, n = len(grid), len(grid[0])
        aux = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                nbrs = [
                    (i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1),
                    (i + 1, j + 1), (i - 1, j + 1), (i - 1, j - 1), (i + 1, j - 1),
                ]
                
                live_count = 0
                for x, y in nbrs:
                    if 0 <= x < m and 0 <= y < n:
                        live_count += grid[x][y]
                
                if grid[i][j]:
                    aux[i][j] = 0 if (live_count < 2 or live_count > 3) else 1
                else:
                    aux[i][j] = 1 if live_count == 3 else 0
                
        
        for i in range(m):
            for j in range(n):
                grid[i][j] = aux[i][j]
        