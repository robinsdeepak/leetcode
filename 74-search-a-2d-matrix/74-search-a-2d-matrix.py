class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        l = m * n
        
        i, j = 0, l - 1
        
        while (i <= j):
            mid = (i + j) // 2
            # print(mid, i, j)
            r, c = mid // n, mid % n
            
            if (matrix[r][c] == target):
                return True
            
            elif (matrix[r][c] > target):
                j = mid - 1
            
            else:
                i = mid + 1
                
        return False
