class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        f = {}
        for char in s:
            if char not in f:
                f[char] = 0
            f[char] += 1
        
        for char in t:
            if char not in f:
                return False
            f[char] -= 1
            if f[char] < 0:
                return False
        
        for k, v in f.items():
            if v != 0:
                return False
        
        return True
