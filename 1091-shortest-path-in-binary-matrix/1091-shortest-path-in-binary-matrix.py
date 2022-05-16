class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]: return -1
        
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        visited = {(0, 0)}
        q = [(0, 0, 1)]
        
        
        while len(q):
            q2 = set()
            for x, y, d in q:
                if x == y == n - 1:
                    return d
                
                for dx, dy in dirs:
                    x2, y2 = x + dx, y + dy
                    if 0 <= x2 < n and 0 <= y2 < n and \
                    (x2, y2) not in visited and grid[x2][y2] == 0:
                        
                        visited.add((x2, y2))
                        q2.add((x2, y2, d + 1))
            
            q = q2
            
        return -1
