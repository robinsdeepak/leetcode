def getFreq(word):
    f = {}
    for char in word:
        f[char] = f.get(char, 0) + 1
    return f

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        F = {}
        
        for w in words2:
            f = getFreq(w)
            for k in f:
                F[k] = max(f[k], F.get(k, 0))
        
        ans = []
        for w in words1:
            f = getFreq(w)
            for k in F:
                if f.get(k, 0) < F[k]:
                    break
            else:
                ans.append(w)
        
        return ans
