class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def traverse(r, c):
            q1 = [(r, c)]
            
            while len(q1):
                q2 = set()
                for x, y in q1:
                    # print(x, y)
                    grid[x][y] = False
                    nbrs = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
                    for r, c in nbrs:
                        if 0 <= r < m and 0 <= c < n and grid[r][c] == "1":
                            q2.add((r, c))
                q1 = q2
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = False
                    count += 1
                    traverse(i, j)
        
        return count

        
