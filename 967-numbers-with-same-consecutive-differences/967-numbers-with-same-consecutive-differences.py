class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.ans = []
        
        def backtrack(num):
            if len(num) == n:
                self.ans.append(int(num))
                return
            
            l = int(num[-1])
            
            if k == 0:
                backtrack(num + str(l))
                return
            
            if l + k < 10:
                backtrack(num + str(l + k))
            
            if l - k >= 0:
                backtrack(num + str(l - k))
        
        for i in range(1, 10):
            backtrack(str(i))
        
        return self.ans

