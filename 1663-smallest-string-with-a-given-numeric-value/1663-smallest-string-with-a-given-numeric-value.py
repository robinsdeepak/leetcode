class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        idx = [1] * n
        
        k -= n
        i = n - 1
        
        while k:
            inc = min(k, 25)
            k -= inc
            idx[i] += inc
            i -= 1
        return "".join(map(lambda x: chr(96 + x), idx))

