from functools import lru_cache


def isPredecessor(w1, w2):
    if len(w1) != len(w2) - 1:
        return False
    
    for i in range(len(w2)):
        w3 = w2[:i] + w2[i+1:]
        if w3 == w1:
            return True
        
    return False
    
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        n = len(words)
        
        mat = [[0] * n for _ in range(n)]
        
        words.sort(key=lambda x: (len(x), x))
        
        for i in range(n):
            for j in range(i + 1, n):
                if isPredecessor(words[i], words[j]):
                    mat[i][j] = 1
        
        @lru_cache(None)
        def rec(i):
            ans = 1
            for j in range(i):
                if mat[j][i]:
                    ans = max(ans, rec(j) + 1)
            return ans
        
        return max((rec(i) for i in range(n)))
