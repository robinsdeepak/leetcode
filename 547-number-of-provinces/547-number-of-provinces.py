class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        
        visited = [False] * len(isConnected)
        
        def dfs(i):
            # print(i)
            m = len(isConnected[i])
            for cc in range(m):
                if isConnected[i][cc] and not visited[cc]:
                    visited[i] = True
                    dfs(cc)
            
        n = len(isConnected)
        
        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = True
                dfs(i)
        
        return count

    