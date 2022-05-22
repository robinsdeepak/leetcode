class Solution:
    def countSubstrings(self, s: str) -> int:
        return self.solution_1(s)
        
    
    def solution_1(self, s):
        n = len(s)
        ans = 0
        
        for i in range(n):
            l, h = i, i
            
            while l >= 0 and h < n and s[l] == s[h]:
                ans += 1
                l -= 1
                h += 1
        
        for i in range(n - 1):
            l, h = i, i + 1

            while l >= 0 and h < n and s[l] == s[h]:
                ans += 1
                l -= 1
                h += 1
        
        return ans



    def solution_2(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        ans = n
        
        for i in range(n):
            dp[i][i] = 1
            
        for i in range(1, n):
            if s[i] == s[i - 1]:
                dp[i - 1][i] = 1
                ans += 1
        
        for l in range(3, n + 1):
            for i in range(0, n - l + 1):
                j = i + l - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = 1
                    ans += 1
                
        return ans
