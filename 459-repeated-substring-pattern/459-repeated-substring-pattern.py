class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not str:
            return False
            
        ss = (s * 2)[1:-1]
        return ss.find(s) != -1