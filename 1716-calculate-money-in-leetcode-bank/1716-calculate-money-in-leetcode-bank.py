class Solution:
    def totalMoney(self, n: int) -> int:
        d, r = n // 7, n % 7
        
        return d * 28 + 7 * (d - 1) * d // 2 + r * (d + 1 + d + r) // 2
