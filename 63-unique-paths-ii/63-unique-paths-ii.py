class Solution:    
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if (grid[0][0] or grid[-1][-1]):
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [[0 for i in range(cols)] for j in range(rows)]
        
        val = 1
        for i in range(rows):
            if (grid[i][0]):
                val = 0
            dp[i][0] = val
        
        val = 1
        for i in range(cols):
            if (grid[0][i]):
                val = 0
            dp[0][i] = val
        # print(dp)
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = 0 if grid[i][j] else dp[i-1][j] + dp[i][j-1]
            
        return dp[rows-1][cols-1]
