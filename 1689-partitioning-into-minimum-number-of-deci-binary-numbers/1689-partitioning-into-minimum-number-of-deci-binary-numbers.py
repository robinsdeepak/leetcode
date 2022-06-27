class Solution:
    def minPartitions(self, n: str) -> int:
        return self.solution_3(n)
    
    def solution_1(self, n):
        return int(max(n))
        
    def solution_2(self, n):
        ans = 1
        for c in n:
            if c == '9':
                return 9
            if int(c) > ans:
                ans = int(c)
        return ans
    
    def solution_3(self, n):
        s = '987654321'
        for c in s:
            if c in n:
                return int(c)
        