class Solution:
    def totalMoney(self, n: int) -> int:
        d, r = n // 7, n % 7
        
        return d * 21 + 7 * d * (d + 1) // 2 + \
               d * r  +     r * (r + 1) // 2
