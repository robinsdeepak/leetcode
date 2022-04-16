class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        adj = {i : [] for i in range(-1, n)}
        mt = -1 
        
        for i in range(n):
            adj[manager[i]].append(i)
        
        def dfs(i, d):
            nonlocal mt
            mt = max(mt, d)
            for j in adj[i]:
                dfs(j, d + informTime[j])
                
        
        dfs(-1, 0)

        return mt
