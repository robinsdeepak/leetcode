class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.solution_2(cost)
        
    def solution_1(self, cost):
        n = len(cost)
        dp = {}
        
        def solve(i):
            if i >= n:
                return 0
            
            if i not in dp:
                dp[i] = cost[i] + min(solve(i + 1), solve(i + 2))
            
            return dp[i]
        
        return min(solve(0), solve(1))
    
    def solution_2(self, cost):
        n = len(cost)
        dp = [-1] * (n + 2)
        dp[-1] = 0
        dp[-2] = 0
        
        
        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])
