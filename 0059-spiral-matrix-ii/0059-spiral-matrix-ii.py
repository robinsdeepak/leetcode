class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        mat = [[0] * n for _ in range(n)]
        
        rs = 0
        cs = 0
        
        re = n - 1
        ce = n - 1
        
        k = 1
        
        for l in range(n // 2 + 1):
            
            # left -> right (top most row)
            for j in range(cs, ce + 1):
                mat[rs][j] = k
                k += 1
            
            rs += 1
            
            # top -> dow (right most col)
            for i in range(rs, re + 1):
                mat[i][ce] = k
                k += 1
            
            ce -= 1
            
            
            # right -> left (bottom most row)
            for j in range(ce, cs - 1, -1):
                mat[re][j] = k
                k += 1
            
            re -= 1
            
            
            # bottom -> up (left most col)
            for i in range(re, rs - 1, -1):
                mat[i][cs] = k
                k += 1
            
            cs += 1
            
            
        return mat
