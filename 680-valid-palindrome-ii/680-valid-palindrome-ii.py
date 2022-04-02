class Solution:
    
    
    def validPalindrome(self, s: str) -> bool:
        def check(st):
            for i in range(len(st)//2):
                if st[i] != st[len(st)-1-i]:
                    return False
            return True
        
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                if check(s[i:len(s)-1-i]) or check(s[i+1:len(s)-i]):
                    return True
                else:
                    return False
        return True

