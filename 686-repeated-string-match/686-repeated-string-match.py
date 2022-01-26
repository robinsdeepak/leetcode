class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        count = 0
        s = ""
        while (len(s) < len(b)):
            s += a
            count += 1
        
        if b in s:
            return count
        elif b in s + a:
            return count + 1
        else:
            return -1
    