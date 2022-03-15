class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        fc, bc, res = 0, 0, ""
        
        for char in s:
            fc += char == '('
            bc += char == ')'
            
            if fc < bc:
                bc -= 1
            else:
                res += char
            
        s = res
    
        fc, bc, res = 0, 0, ""
        
        for char in reversed(s):
            fc += char == '('
            bc += char == ')'
            
            if fc > bc:
                fc -= 1
            else:
                res += char
            
        
        return res[::-1]

