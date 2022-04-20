def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


class Solution:
    def canMeasureWater(self, j1, j2, t):
        if t > j1 + j2: return False
        if t in [j1, j2, j1 + j2]:
            return True
        
        return t % gcd(j1, j2) == 0
