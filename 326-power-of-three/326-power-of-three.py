class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return self.solution_2(n)
    
    def solution_1(self, n):
        while n > 1:
            if n % 3:
                return False
            n //= 3
        
        return n == 1
    
    def solution_2(self, n):
        p3 = {
            1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147,
            531441, 1594323, 4782969, 14348907, 43046721, 129140163, 
            387420489, 1162261467, 3486784401
        }
        return n in p3
