class Solution:        
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for x in num:
            while len(stack) > 0 and k > 0 and stack[-1] > x:
                stack.pop()
                k -= 1
            if len(stack) or x != 0:
                stack.append(x)
                
        while len(stack) and k > 0:
            stack.pop()
            k -= 1
            
        if not len(stack):
            return "0"
        return str(int("".join(stack)))

    