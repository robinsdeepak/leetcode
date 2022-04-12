class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        inf = 100000
        dist = [[inf] * n for _ in range(m)]
        
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
                    visited[i][j] = True
        
        d = 0
        while len(q):
            q2 = []
            for x, y in q:
                nbrs = [
                    (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
                    # (x + 1, y + 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1)
                ]
                
                for i, j in nbrs:
                    if 0 <= i < m and 0 <= j < n and dist[i][j] > dist[x][y]:
                        q2.append((i, j))
                        dist[i][j] = dist[x][y] + 1
                        visited[i][j] = True
            q = q2
            d += 1

        return dist
