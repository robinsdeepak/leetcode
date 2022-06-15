from functools import lru_cache

    
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words = set(words)
        
        @lru_cache(None)
        def rec(w):
            ans = 1
            for i in range(len(w)):
                w2 = w[:i] + w[i+1:]
                if w2 in words:
                    ans = max(ans, rec(w2) + 1)
            return ans
                
        return max(map(rec, words))
