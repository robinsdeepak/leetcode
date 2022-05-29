class Solution:
    
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        
        def bits(w):
            x = 0
            for c in w:
                x |= (1 << (ord(c) - 97))
            return x
        
        freq = []
        for w in words:
            freq.append((bits(w), len(w)))
                
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if not (freq[i][0] & freq[j][0]):
                    ans = max(ans, (freq[i][1] * freq[j][1]))
        
        return ans

