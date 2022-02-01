class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        fresh_count = 0
        q = {0: []}
        t = 0
        
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 2):
                    q[t].append((i, j))
                elif (grid[i][j] == 1):
                    fresh_count += 1
        
        while (t < len(q) and fresh_count > 0):
            for i, j in q[t]:
                adj = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
                
                for i2, j2 in adj:
                    if not (0 <= i2 < m and 0 <= j2 < n):
                        continue
                    
                    if (grid[i2][j2] == 1):
                        grid[i2][j2] = 2
                        if (t + 1) not in q:
                            q[t + 1] = []
                        q[t + 1].append((i2, j2))
                        fresh_count -= 1
            t = t + 1
        
        return -1 if fresh_count else t
