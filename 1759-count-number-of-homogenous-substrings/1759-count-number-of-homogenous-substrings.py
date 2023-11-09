class Solution:
    def countHomogenous(self, s: str) -> int:
        m = 10 ** 9 + 7
        
        def nsum(n):
            return ((n + 1) * n // 2) % m
        
        cc = 0
        lc = ""
        ans = 0

        for char in s:
            if char == lc:
                cc += 1
            else:
                ans = (ans + nsum(cc)) % m
                cc = 1
                lc = char
                
        ans = (ans + nsum(cc)) % m
        
        return ans
