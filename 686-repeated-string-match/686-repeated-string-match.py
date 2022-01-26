class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        count = -(-(len(b)) // len(a))
        s = a * count
        
        for i in range(2):
            if b in (s + a * i):
                return count + i
        return -1

    