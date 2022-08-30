class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        e = n - 1
        for i in range((n + 1) // 2):
            for j in range(n // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[e - j][i]
                matrix[e - j][i] = matrix[e - i][e - j]
                matrix[e - i][e - j] = matrix[j][e - i]
                matrix[j][e - i] = tmp

