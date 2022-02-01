class Solution:
    def __init__(self):
        self.ans = 0
        self.map = {}
    
    def set_val(self, x, y, val):
        if x not in self.map:
            self.map[x] = {}
        self.map[x][y] = val
    
    def get_val(self, x, y):
        return self.map.get(x, {}).get(y)
    
    def solve(self, grid, x, y):
        # print(x, y)
        if (x == 0 and y == 0):
            return 1
        if (x < 0 or y < 0 or grid[x][y] == 1):
            return 0
        
        if (self.get_val(x, y)):
            return self.get_val(x, y)
        
        val = self.solve(grid, x - 1, y) + self.solve(grid, x, y - 1)
        self.set_val(x, y, val)
        return val
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if (obstacleGrid[0][0] == 1):
            return 0
        return self.solve(obstacleGrid, len(obstacleGrid)-1, len(obstacleGrid[0])-1)
