class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        return self.solution_2(matrix)
    
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
