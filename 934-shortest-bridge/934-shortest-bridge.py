class Solution:
    def shortestBridge(self, grid):
        m, n = len(grid), len(grid[0])
        
        def firstLand():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1: return (i, j)
        
        q = [[*firstLand(), 2]]
        l1 = [] + q
        
        while len(q):
            l1 += q
            q2 = set()
            for i, j, d in q:
                grid[i][j] = 2
                nbrs = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
                
                for x, y in nbrs:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        q2.add((x, y, 2))
            q = q2

        q = l1 
        while len(q):
            q2 = set()
            for i, j, d in q:
                grid[i][j] = d
                nbrs = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
                for x, y in nbrs:
                    if 0 <= x < m and 0 <= y < n:
                        if grid[x][y] == 1:
                            return d - 2
                        if grid[x][y] == 0:
                            q2.add((x, y, d + 1))
            q = q2
        return -1
