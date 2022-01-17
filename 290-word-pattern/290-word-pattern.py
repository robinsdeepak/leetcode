class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        p1 = list(pattern)
        s1 = string.split()
                
        if (len(p1) != len(s1)):
            return False
        
        d = {}
        
        for p, s in  zip(p1, s1):
            if p not in d:
                d[p] = s
            if d[p] != s:
                return False
            
        return len(set(d.values())) == len(d)
