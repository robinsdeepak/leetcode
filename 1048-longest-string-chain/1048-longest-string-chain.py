from functools import lru_cache

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words = set(words)
        
        @lru_cache(None)
        def dp(w):
            ans = 1
            for i in range(len(w)):
                pw = w[:i] + w[i+1:]
                if pw in words:
                    ans = max(ans, dp(pw) + 1)
            return ans
        
        return max((dp(w) for w in words))
