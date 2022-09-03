class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
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
