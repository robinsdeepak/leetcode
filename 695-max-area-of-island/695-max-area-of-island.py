class Solution:
    def __init__(self):
        self.visited = []
        
    def solve(self, grid, rows, cols, x, y):
        if not ((0 <= x < rows) and (0 <= y < cols) and grid[x][y] and not self.visited[x][y]):
            return 0
        self.visited[x][y] = 1
        return 1 +  self.solve(grid, rows, cols, x + 1, y) + \
                    self.solve(grid, rows, cols, x, y + 1) + \
                    self.solve(grid, rows, cols, x - 1, y) + \
                    self.solve(grid, rows, cols, x, y - 1)
        
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.visited = [[0 for i in range(cols)] for j in range(rows)]
        max_area = 0
        for x in range(rows):
            for y in range(cols):
                if (grid[x][y] == 1 and self.visited[x][y] == 0):
                    max_area = max(max_area, self.solve(grid, rows, cols, x, y))
        return max_area
    
    
    