class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        p1 = list(pattern)
        s1 = string.split()
                
        if (len(p1) != len(s1)):
            return False
        
        d1 = {}
        d2 = {}
        
        for p, s in  zip(p1, s1):
            if p not in d1:
                d1[p] = s
            if d1[p] != s:
                return False
            
            if s not in d2:
                d2[s] = p
            if d2[s] != p:
                return False
        
        return True
            