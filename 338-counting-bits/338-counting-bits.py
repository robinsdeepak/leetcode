class Solution:
    def bitCount(self, x):
        count = 0
        while x:
            count += (x & 1)
            x >>= 1
        return count

    def countBits(self, n: int) -> List[int]:
        return [self.bitCount(i) for i in range(n + 1)]

