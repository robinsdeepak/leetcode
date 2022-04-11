class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        v1 = [[0] * n for _ in range(m)]
        v2 = [[0] * n for _ in range(m)]
        
        
        q1 = []
        q2 = []
        
        for i in range(m):
            q1.append((i, 0))
            q2.append((i, n - 1))
        
        for j in range(n):
            q1.append((0, j))
            q2.append((m - 1, j))
        
        
        def dfs1(x, y):
            v1[x][y] = 1
            
            nbrs = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

            for i, j in nbrs:
                if i < 0 or i >= m or j < 0 or j >= n:
                    continue
                
                if not v1[i][j] and heights[x][y] <= heights[i][j]:
                    dfs1(i, j)
        
            
        def dfs2(x, y):
            v2[x][y] = 1
            
            nbrs = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            
            for i, j in nbrs:
                if i < 0 or i >= m or j < 0 or j >= n:
                    continue 
                
                if not v2[i][j] and heights[x][y] <= heights[i][j]:
                    dfs2(i, j)
        
        for x, y in q1:
            if not v1[x][y]:
                dfs1(x, y)
        
        for x, y in q2:
            if not v2[x][y]:
                dfs2(x, y)
        
        result = []
        
        for i in range(m):
            for j in range(n):
                if v1[i][j] and v2[i][j]:
                    result.append((i, j))
        
        
        return result
