class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        
        for i, j in connections:
            g[i].append((j, True))
            g[j].append((i, False))
        
        
        visited_from = set()
        self.count = 0
        
        def dfs(i):
            if i in visited_from:
                return
            
            visited_from.add(i)
            
            for j, isCon in g[i]:
                if j not in visited_from:
                    if isCon:
                        self.count += 1
                    dfs(j)

        dfs(0)
        
        return self.count
