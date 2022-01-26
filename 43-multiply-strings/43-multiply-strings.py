class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        i2s = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        s2i = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        n1 = 0
        for s in num1:
            n1 = n1 * 10 + s2i[s]
        
        n2 = 0
        for s in num2:
            n2 = n2 * 10 + s2i[s]
        
        product = n1 * n2
        if (product == 0): return "0"
    
        sp = ""
        while (product):
            sp += i2s[product % 10]
            product //= 10
        
        return "".join(sp[::-1])
    
        