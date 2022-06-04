class Solution:
    
    def __init__(self):
        self.board = None
        self.ans = []
    
    def isValid(self, i, j, n):
        for r in range(i):
            if self.board[r][j] == 'Q':
                return False
        
        for c in range(n):
            if self.board[i][c] == 'Q':
                return False
        
        dirs = ((-1, -1), (-1, 1))
        corners = [(i, j, ii) for ii in range(2)]
        
        while corners:
            c2 = []
            for i, j, ii in corners:
                x = i + dirs[ii][0]
                y = j + dirs[ii][1]
                
                if not (0 <= x < n and 0 <= y < n):
                    continue
                
                if self.board[x][y] == 'Q':
                    return False
                
                c2.append((x, y, ii))
            
            corners = c2
        
        return True
    
    def solve(self, i, n):
        if i == n:
            curr_ans = [''.join(row) for row in self.board]
            self.ans.append(curr_ans)
            return True
        
        for j in range(n):
            if self.isValid(i, j, n):
                self.board[i][j] = 'Q'
                self.solve(i + 1, n)
                self.board[i][j] = '.'
        
        return False
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [['.'] * n for _ in range(n)]
        self.solve(0, n)
        return self.ans

