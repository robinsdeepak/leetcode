from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.solution_2(matrix, target)
    
    def solution_1(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        
        for r in range(m):
            idx = bisect_left(matrix[r], target)
            if idx < n and matrix[r][idx] == target:
                return True
        
        return False

    
    def solution_2(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        r, c = m - 1, 0
        
        while r >= 0 and c < n:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c = bisect_left(matrix[r], target)
            else:
                return True
        
        return False
