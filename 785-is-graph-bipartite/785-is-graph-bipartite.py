class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n
        
        def dfs(i):
            for j in graph[i]:
                if colors[j] == colors[i]:
                    return False
                elif colors[j] == -1:
                    colors[j] = 1 - colors[i]
                
                    if not dfs(j):
                        return False
            
            return True
        
        for i in range(n):
            if colors[i] == -1:
                colors[i] = 0
                if not dfs(i):
                    return False
        return True
