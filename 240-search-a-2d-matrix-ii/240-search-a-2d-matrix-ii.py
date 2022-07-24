from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        for r in range(m):
            idx = bisect_left(matrix[r], target)
            if idx < n and matrix[r][idx] == target:
                return True
        
        return False
