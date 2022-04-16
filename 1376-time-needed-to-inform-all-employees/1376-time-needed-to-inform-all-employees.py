class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        adj = {i : [] for i in range(-1, n)}
        mt = -1 
        
        for i in range(n):
            adj[manager[i]].append(i)
        
        q = [(-1, 0)]
        
        while len(q):
            q2 = []
            
            for i, d in q:
                mt = max(mt, d)
                for j in adj[i]:
                    q2.append((j, d + informTime[j]))
            q = q2
            
        return mt
