class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        m = {}
        ans = -1
        
        for i, c in enumerate(s):
            if c in m:
                ans = max(ans, i - m[c] - 1)
            else:
                m[c] = i
        return ans
