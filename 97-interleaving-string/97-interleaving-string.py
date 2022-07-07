from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        @lru_cache(None)
        def rec(t1, t2, t3):
            # print(t1, t2, t3)
            
            if not t1:
                return t2 == t3
            
            if not t2:
                return t1 == t3
            
            if t1[0] == t2[0] == t3[0]:
                return rec(t1[1:], t2, t3[1:]) or rec(t1, t2[1:], t3[1:])
            
            elif t1[0] == t3[0]:
                return rec(t1[1:], t2, t3[1:])
                
            
            elif t2[0] == t3[0]:
                return rec(t1, t2[1:], t3[1:])
            
            return False
        
        return rec(s1, s2, s3)
