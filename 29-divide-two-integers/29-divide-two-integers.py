class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        factor = (-1) ** ((dividend < 0) ^ (divisor < 0))
        dividend, divisor = abs(dividend), abs(divisor)
        maxnum = 2147483647
        
        if divisor == 1:
            return min(factor * dividend, maxnum)
        
        while dividend >= divisor:
            
            dvd, dvs = dividend, divisor
            m = 1
            while dvd >= (dvs << 1):
                dvs <<= 1
                m <<= 1
            
            ans += m
            dividend -= dvs
            # print(dvs)
        
        return min(factor * ans, maxnum)
