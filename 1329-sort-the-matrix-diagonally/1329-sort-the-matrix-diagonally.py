class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        start_coords = [(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)]
        
        for sr, sc in start_coords:
            elements = []
            r, c = sr, sc
            
            while r < m and c < n:
                elements.append(mat[r][c])
                r += 1
                c += 1
                
            elements.sort()
            
            k = 0
            r, c = sr, sc
            while r < m and c < n:
                mat[r][c] = elements[k]
                r += 1
                c += 1
                k += 1
            
        return mat
