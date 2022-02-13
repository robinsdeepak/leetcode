class Solution:
    
    def solve(self, board, word, x, i, j):
        
        if (x >= len(word)):
            return True
        
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return False
        
        if (board[i][j] == word[x]):
            board[i][j] = "-1"
            solved = self.solve(board, word, x + 1, i, j + 1) or \
                    self.solve(board, word, x + 1, i, j - 1) or \
                    self.solve(board, word, x + 1, i + 1, j) or \
                    self.solve(board, word, x + 1, i - 1, j)
            board[i][j] = word[x]
            return solved
        return False
        
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.solve(board, word, 0, i, j):
                    return True
        return False

