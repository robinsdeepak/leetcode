class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        q = [(i, i) for i in range(n)]
        ans = (s[0], 1)
        
        for i in range(1, n):
            if s[i - 1] == s[i]:
                q.append((i - 1, i))
                ans = (s[i-1:i+1], 2)
                
        while len(q):
            q2 = []
            
            for i, j in q:
                i2, j2 = i - 1, j + 1
                if i2 >= 0 and j2 < n and s[i2] == s[j2]:
                    q2.append((i2, j2))
                    l = j2 - i2 + 1
                    if l > ans[1]:
                        ans = (s[i2:j2+1], l)
            q = q2
            
        return ans[0]
    