class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = {}
        
        q = []
        
        for i in range(m):
            q.append((i, 0))
            q.append((i, n - 1))
        
        for j in range(1, n - 1):
            q.append((0, j))
            q.append((m - 1, j))
        
        q = [(i, j) for i, j in q if grid[i][j]]
        
        while len(q):
            q2 = set()
            
            for x, y in q:
                grid[x][y] = 0
                
                nbrs = [(x+1, y), (x, y+1), (x-1,y), (x, y-1)]
                
                for r, c in nbrs:
                    if 0 <= r < m and 0 <= c < n and grid[r][c]:
                        q2.add((r, c))
            q = q2
        
        # print(grid)
        count = 0
        for i in range(m):
            for j in range(n):
                count += grid[i][j]
        
        return count
