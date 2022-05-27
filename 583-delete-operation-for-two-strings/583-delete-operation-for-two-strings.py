class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
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
