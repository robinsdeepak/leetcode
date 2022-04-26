class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mat = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d2 = abs(x1 - x2)  + abs(y1 - y2) 
                mat[i][j] = mat[j][i] = d2
        
        keys = [float('inf')] * n
        keys[0] = 0
        mset = [False] * n
        cost = 0
        
        for i in range(n):
            msi = -1
            for j in range(n):
                if not mset[j] and (msi == -1 or keys[msi] > keys[j]):
                    msi = j
            
            cost += keys[msi]
            mset[msi] = True
            
            for j in range(n):
                if not mset[j] and mat[msi][j]:
                    keys[j] = min(keys[j], mat[msi][j])
            
        return cost
