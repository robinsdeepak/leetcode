class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        m = len(connections)
        
        if m < n - 1:
            return -1
        
        adj = [[] for _ in range(n)]
        
        for i, j in connections:
            adj[i].append(j)
            adj[j].append(i)
        # print(adj)
        visited = [False] * n
        
        def dfs(i):
            # print(i, adj[i])
            for j in adj[i]:
                if not visited[j]:
                    visited[j] = True
                    dfs(j)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = True
                dfs(i)
        dfs(0)
        # print(n, sum(visited), count)
        return n - sum(visited) + count - 1
