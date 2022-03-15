class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        fc = 0
        bc = 0
        
        s2 = ""
        
        for char in s:
            fc += char == '('
            bc += char == ')'
            
            if fc < bc:
                bc -= 1
            else:
                s2 += char
            
#             print(s2)
        
#         print("===========================")

        fc, bc = 0, 0
        s = s2
        s2 = ""
        
        for char in s[::-1]:
            fc += char == '('
            bc += char == ')'
            
            if fc > bc:
                fc -= 1
            else:
                s2 += char
            
            # print(s2)
        
        return s2[::-1]

