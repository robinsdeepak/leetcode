from functools import lru_cache

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int):
        inf = float('inf')
        
        @lru_cache(None)
        def rec(i, p, t):
            if t == -1:
                return inf
            if i == -1:
                return 0 if t == 0 else inf
            
            if houses[i] != 0:
                ct = t if p == houses[i] else t - 1
                return rec(i - 1, houses[i], ct)
            
            c = inf
            for j in range(1, n + 1):
                cc = cost[i][j - 1]
                ct = t
                if p != j:
                    ct -= 1
                    
                c = min(c, rec(i - 1, j, ct) + cc)
            return c
        
        ans = rec(m - 1, -1, target)
        return -1 if ans == inf else ans

