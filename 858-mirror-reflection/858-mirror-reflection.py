class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if q == 0: return 0
        if p == q: return 1
        

        lcm = (p * q) // gcd(p, q) 
        
        n1 = lcm // p
        n2 = lcm // q
        
        if n2 % 2 == 0:
            return 2
        
        if n1 % 2 == 0:
            return 0
        
        return 1
    
def gcd(a, b):        
    while a != 0:
        a, b = b % a, a
    return b

