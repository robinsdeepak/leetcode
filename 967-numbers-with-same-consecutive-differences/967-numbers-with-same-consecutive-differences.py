class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        return self.solution_2(n, k)
        
    def solution_1(self, n, k):
        self.ans = []
        
        def rec(num, l, c):
            if c == n:
                self.ans.append(num)
                return
                        
            if k == 0:
                rec(num * 10 + l, l, c + 1)
                return
            
            if l + k < 10:
                rec(num * 10 + (l + k), (l + k), c + 1)
            
            if l - k >= 0:
                rec(num * 10 + (l - k), (l - k), c + 1)
        
        for i in range(1, 10):
            rec(i, i, 1)
        
        return self.ans
    
    def solution_2(self, n, k):
        if k == 0:
            return list(map(lambda x: int(str(x) * n), range(1, 10)))
        
        numbers = list(range(1, 10))
        
        for _ in range(n - 1):
            numbers2 = []
            for x in numbers:
                l = x % 10
                if l + k < 10:
                    numbers2.append(x * 10 + (l + k))
                if l - k >= 0:
                    numbers2.append(x * 10 + (l - k))
            numbers = numbers2
        
        return numbers

