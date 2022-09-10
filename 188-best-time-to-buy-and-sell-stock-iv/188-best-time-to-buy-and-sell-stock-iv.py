from functools import lru_cache

class Solution:
    def dp(self, prices, currentDay, remainingTransactions, holding, lookup):
        # Return 0 if there aren't any transactions left or there are no more stocks.
        if remainingTransactions == 0 or currentDay == len(prices):
            return 0
        if not lookup[currentDay][remainingTransactions][holding]:
            if holding:
                # Return max(did nothing on current day, sold all the stocks on current day).
                lookup[currentDay][remainingTransactions][holding] = max(self.dp(prices, currentDay+1, remainingTransactions, holding, lookup), prices[currentDay] + self.dp(prices, currentDay+1, remainingTransactions-1, 0, lookup))
            else:
                # Return max(did nothing on current day, bought all the stocks on current day).
                lookup[currentDay][remainingTransactions][holding] = max(self.dp(prices, currentDay+1, remainingTransactions, holding, lookup), -prices[currentDay] + self.dp(prices, currentDay+1, remainingTransactions, 1, lookup))
        return lookup[currentDay][remainingTransactions][holding]
            
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.dp(prices, 0, k, 0, [[[None for _ in range(2)] for _ in range(k+1)] for _ in range(len(prices))])
        
    def solution_1(self, k, prices):
        n = len(prices)
        self.dp = {}
        
        def solve(idx, last, rem):
            if idx == n or rem < 0:
                return 0
            
            key = (idx, last, rem)
            if key in self.dp:
                return self.dp[key]
            
            if last == -1:
                self.dp[key] = max(
                    solve(idx + 1, idx, rem - 1),
                    solve(idx + 1, -1, rem)
                )
            else:
                self.dp[key] = max(
                    solve(idx + 1, -1, rem) + (prices[idx] - prices[last]),
                    solve(idx + 1, last, rem)
                )
            
            return self.dp[key]
        
        return solve(0, -1, k)

