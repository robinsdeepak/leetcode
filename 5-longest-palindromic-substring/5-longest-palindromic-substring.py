class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 1
        ans = s[0]
        
        for l in range(2):
            for c in range(n):
                i, j = c, c + l
                while i >= 0 and j < n and s[i] == s[j]:
                    i -= 1
                    j += 1
                
                curr = j - i - 1
                if curr > maxLen:
                    ans = s[i+1:j]
                    maxLen = curr
                
        return ans
