class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        
        rbegin, rend = 0, n - 1
        cbegin, cend = 0, n - 1
        k = 1
        while (rbegin <= rend and cbegin <= cend):
            for col in range(cbegin, cend + 1):
                matrix[rbegin][col] = k
                k += 1
                
            rbegin += 1
            
            for row in range(rbegin, rend + 1):
                matrix[row][cend] = k
                k += 1
                
            cend -= 1
            
            if (rbegin <= rend):
                for col in range(cend, cbegin - 1, -1):
                    matrix[rend][col] = k
                    k += 1
            rend -= 1
            
            if (cbegin <= cend):
                for row in range(rend, rbegin - 1, -1):
                    matrix[row][cbegin] = k
                    k += 1
            cbegin += 1       
            
        return matrix
    
