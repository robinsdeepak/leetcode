from functools import lru_cache

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int):
        inf = float('inf')
        
        @lru_cache(None)
        def rec(i, p, t):
            if t == -1: 
                return inf
            if i == -1:
                if t == 0:
                    return 0
                else:
                    return inf
            
            if houses[i] != 0:
                return rec(i - 1, houses[i], t - (p != houses[i]))
            
            return min(rec(i - 1, j, t - (p != j)) + cost[i][j - 1] for j in range(1, n + 1))
        
        ans = rec(m - 1, -1, target)
        return -1 if ans == inf else ans

