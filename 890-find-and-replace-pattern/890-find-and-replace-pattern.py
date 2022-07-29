def encode(w):
    m = {}
    c = 0
    out = ""
    for char in w:
        if char not in m:
            m[char] = c
            c += 1
        out += str(m[char])
    return out


class Solution:
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        pe = encode(pattern)
        
        ans = []
        
        for word in words:
            if encode(word) == pe:
                ans.append(word)
        
        return ans
