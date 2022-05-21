from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = float('inf')
        coins.sort(reverse=True)
        
        @lru_cache(maxsize=None)
        def solve(ci, t):
            if t == 0:
                return 0
            
            if t < 0 or ci < 0:
                return inf
            
            n1 = solve(ci - 1, t)
            n2 = solve(ci, t - coins[ci]) + 1
            
            return min(n1, n2)
        
        ans = solve(len(coins) - 1, amount)
        ans = -1 if ans == inf else ans
        return ans

