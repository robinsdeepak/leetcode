class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        
        def dfs(x, i, j):
            if (x == len(word)):
                return True
            
            if (i < 0 or i >= m or j < 0 or j >= n or word[x] != board[i][j]):
                return False
            
            board[i][j] = "-"
            solved = dfs(x + 1, i, j + 1) or \
                     dfs(x + 1, i, j - 1) or \
                     dfs(x + 1, i + 1, j) or \
                     dfs(x + 1, i - 1, j)
            
            board[i][j] = word[x]
            return solved
        
        for r in range(m):
            for c in range(n):
                if dfs(0, r, c):
                    return True
        return False

