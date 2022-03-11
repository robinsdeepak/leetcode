class Solution:
    dp = {}
    
    def climbStairs(self, n: int) -> int:
        if (n < 0):
            return 0
        if (n == 0):
            return 1
        if self.dp.get(n):
            return self.dp.get(n)
        
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]
