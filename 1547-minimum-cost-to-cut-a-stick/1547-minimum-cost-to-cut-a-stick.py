from functools import lru_cache

class Solution:
    
    
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        
        
        @lru_cache(maxsize=None)
        def solve(i, j):            
            if i > j:
                return 0
            
            ans = float('inf')
            
            for x in range(i, j + 1):
                curr = solve(i, x - 1) + \
                       solve(x + 1, j) + \
                       cuts[j + 1] - cuts[i - 1]
                
                ans = min(curr, ans)
            
            
            return ans
        
        return solve(1, len(cuts) - 2)

