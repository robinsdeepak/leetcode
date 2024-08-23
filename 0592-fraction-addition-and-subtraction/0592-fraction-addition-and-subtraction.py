from fractions import Fraction


class Solution:
    def fractionAddition(self, expression: str) -> str:
        sign = 1
        result = 0
        nums = ['']
        for c in expression:
            if c in ('-', '+'):
                if nums[-1]:
                    a, b = nums.pop().split('/')
                    result = result + Fraction(int(a), int(b)) * sign
                nums.append('')
                if c == '-':
                    sign = -1
                if c == '+':
                    sign = +1
            else:
                nums[-1] += c

        if len(nums) and nums[-1]:
            a, b = nums.pop().split('/')
            result = result + Fraction(int(a), int(b)) * sign

        result = str(result)
        if '/' not in result:
            result = result + '/1'
        return result
