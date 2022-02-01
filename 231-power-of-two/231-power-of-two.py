class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while (x < n):
            x <<= 1
            if (x == n):
                return True
        return x == n
