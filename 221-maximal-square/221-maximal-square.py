class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        return self.solution_0(matrix)
    
    def solution_0(self, matrix):
        m, n = len(matrix), len(matrix[0])
        size = 0
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or matrix[i][j] == "0":
                    matrix[i][j] = int(matrix[i][j])
                else:
                    matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) + 1
            
                size = max(size, matrix[i][j])
        
        return size * size
    
    def solution_1(self, matrix):
        m, n = len(matrix), len(matrix[0])
        
        dp = [[0] * n for _ in range(m)]
        size = 0
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or matrix[i][j] == "0":
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
            
                size = max(size, dp[i][j])
        
        return size * size

    def solution_2(self, matrix):
        m, n = len(matrix), len(matrix[0])
        
        dp = [0] * n
        size = 0
        
        for i in range(m):
            temp = [0] * n
            for j in range(n):
                if i == 0 or j == 0 or matrix[i][j] == "0":
                    temp[j] = int(matrix[i][j])
                else:
                    temp[j] = min(dp[j - 1], temp[j - 1], dp[j]) + 1
            
                size = max(size, temp[j])
            dp = temp
        
        return size * size
    
    def solution_3(self, matrix):
        m, n = len(matrix), len(matrix[0])
        size = 0
        
        @lru_cache(maxsize=None)
        def rec(i, j):
            if i == 0 or j == 0 or matrix[i][j] == "0":
                curr = int(matrix[i][j])
            else:
                curr = min(rec(i, j - 1), rec(i - 1, j), rec(i - 1, j - 1)) + 1
            nonlocal size
            size = max(size, curr)
            return curr
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                rec(i, j)
        
        return size * size

