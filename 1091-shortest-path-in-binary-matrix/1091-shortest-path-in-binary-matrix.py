class Solution:
     
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        
        q = [(0, 0, 1)]
        
        while len(q):
            q2 = []
            
            for i, j, d in q:
                if i == j == n - 1:
                    return d
                
                nbrs = ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1))

                for x, y in nbrs:
                    if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                        grid[x][y] = 1
                        q2.append((x, y, d+1))
            q = q2
        
        return -1
