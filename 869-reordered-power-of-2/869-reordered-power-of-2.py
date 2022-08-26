class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        x = 1
        sn = ''.join(sorted(str(n), reverse=True))        
        n2 = int(sn)
        
        while x <= n2:
            if ''.join(sorted(str(x), reverse=True)) == sn:
                return True
            x <<= 1
        
        return False
