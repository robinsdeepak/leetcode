class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        return self.solution_3(w1, w2)
    
    def solution_3(self, w1, w2):
        n1, n2 = len(w1), len(w2)
        memo = [0] * (n2 + 1)
        
        for i in range(n1 + 1):
            temp = [0] * (n2 + 1)
            for j in range(n2 + 1):
                if (i == 0 or j == 0):
                    temp[j] = i + j
                    
                elif w1[i - 1] == w2[j - 1]:
                    temp[j] = memo[j - 1]
                    
                else:
                    temp[j] = min(memo[j], temp[j - 1]) + 1
            
            memo = temp
        
        return memo[n2]
        
        
    def solution_2(self, w1, w2):
        n1, n2 = len(w1), len(w2)
        memo = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if (i == 0 or j == 0):
                    memo[i][j] = i + j
                    
                elif w1[i - 1] == w2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                    
                else:
                    memo[i][j] = min(memo[i - 1][j], memo[i][j - 1]) + 1
        
        return memo[n1][n2]

    def solution_1(self, w1, w2):
        n1, n2 = len(w1), len(w2)
        memo = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if w1[i - 1] == w2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1] + 1
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
                
        return n1 + n2 - memo[n1][n2] * 2
