class Solution:
    def calcEquation(self, equations, values, queries):
        
        varrs = {c: i for i, c in enumerate(sorted(list(set(sum(equations, [])))))}
        
        n = len(varrs)
        
        g = [[-1] * n for _ in range(n)]
        
        for xy, v in zip(equations, values):
            x, y = xy
            g[varrs[x]][varrs[y]] = v
            g[varrs[y]][varrs[x]] = 1 / v
            
        
        def dfs(src, dest, visited):
            if src == dest:
                return 1.0;
            
            visited.add(src)
            
            for i in range(n):
                if g[src][i] != -1 and i not in visited:
                    ans = dfs(i, dest, visited)
                    if ans != -1.0:
                        return ans * g[src][i]        
            return -1.0
        
        result = []
        for s, d in queries:
            if s not in varrs or d not in varrs:
                result.append(-1.0)
                continue
            src, dest = varrs[s], varrs[d]
            curr = dfs(src, dest, set())
            result.append(curr)
        return result
