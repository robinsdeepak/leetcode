class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        rows = len(matrix)
        cols = len(matrix[0])
        
        rbegin, rend = 0, rows - 1
        cbegin, cend = 0, cols - 1
        
        while (rbegin <= rend and cbegin <= cend):
            arr.extend([matrix[rbegin][col] for col in range(cbegin, cend + 1)])
            rbegin += 1
            
            arr.extend([matrix[row][cend] for row in range(rbegin, rend + 1)])
            cend -= 1
            
            if (rbegin <= rend):
                arr.extend([matrix[rend][col] for col in range(cend, cbegin - 1, -1)])
            rend -= 1
            
            if (cbegin <= cend):
                arr.extend([matrix[row][cbegin] for row in range(rend, rbegin - 1, -1)])
            cbegin += 1       
            
        return arr
