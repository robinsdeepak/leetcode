from functools import lru_cache

class Solution:
    def coinChangeOld(self, coins: List[int], amount: int) -> int:
        inf = float('inf')
        
        @lru_cache(maxsize=None)
        def solve(ci, t):
            if t == 0:
                return 0
            
            if t < 0 or ci < 0:
                return inf
            
            return min(
                solve(ci - 1, t),
                solve(ci, t - coins[ci]) + 1
            )
        
        ans = solve(len(coins) - 1, amount)
        ans = -1 if ans == inf else ans
        return ans

    def coinChange(self, coins: List[int], amount: int) -> int:
        count, prev = 0, 1 << amount
        while prev & 1 == 0:
            curr = prev
            for coin in coins:
                curr |= prev >> coin
            if curr == prev:
                return -1
            count += 1
            prev = curr
        return count