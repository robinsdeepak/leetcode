class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        self.m, self.n = len(matrix), len(matrix[0])
        
        for i in range(self.m):
            for j in range(1, self.n):
                matrix[i][j] += matrix[i][j - 1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        
        for r in range(row1, row2 + 1):
            s = self.matrix[r][col1 - 1] if col1 > 0 else 0
            e = self.matrix[r][col2]
            ans += (e - s)
        
        return ans



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)