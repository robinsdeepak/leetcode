class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        
        ans = 0
        if n & 1:
            mid = n // 2
            ans = -mat[mid][mid]
                    
        for i in range(n):
            ans += mat[i][i]
            ans += mat[n - 1 - i][i]
        return ans
