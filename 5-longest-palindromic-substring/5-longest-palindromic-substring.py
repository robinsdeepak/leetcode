class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = (1, s[0])
        for i in range(n):
            for j in range(2):
                l, h = i, i + j
                while l >= 0 and h < n and s[l] == s[h]:
                    curr_len = h - l + 1
                    if curr_len > ans[0]:
                        ans = (curr_len, s[l : h + 1])
                    l -= 1
                    h += 1
        return ans[1]
