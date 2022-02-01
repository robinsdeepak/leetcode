class Solution:
    def __init__(self):
        self.count = 0
    
    def isSafe(self, board, idx, val):
        board[idx] = val
        for i in range(len(board)):
            if (i != idx and board[i] == val):
                board[idx] = -1
                return False
        
        for i in range(len(board)-1):
            for j in range(i+1, len(board)):
                if (board[i] != -1 and board[j] != -1 and abs(board[i] - board[j]) == j - i):
                    board[idx] = -1
                    return False
        board[idx] = -1
        return True
    
    def solve(self, board, idx):
        # print(board)
        if (idx == len(board)):
            self.count += 1
            return True
        
        for i in range(len(board)):
            if self.isSafe(board, idx, i):
                board[idx] = i
                self.solve(board, idx + 1)
                board[idx] = -1
            
        return False
    
    
    def totalNQueens(self, n: int) -> int:
        board = [-1 for _ in range(n)]
        self.solve(board, 0)
        return self.count
