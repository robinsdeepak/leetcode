class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        f = Counter(magazine)
        
        for ch in ransomNote:
            if ch not in f or f[ch] == 0:
                return False
            f[ch] -= 1
        
        return True
