class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def traverse(r, c):
            q1 = [(r, c)]
            cn = 1
            
            while len(q1):
                q2 = set()
                for x, y in q1:
                    grid[x][y] = 1

                    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                        cn = 0
                    
                    nbrs = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
                    for r, c in nbrs:
                        if 0 <= r < m and 0 <= c < n and grid[r][c] == 0:
                            q2.add((r, c))
                q1 = q2
            
            return cn
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    t = traverse(i, j)
                    if (t):
                        count += 1
                        # print(i, j, t)
        
        return count
