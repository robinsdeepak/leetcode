class Solution {
public:
    bool solve(vector<vector<char>>& board, string word, int x, int i, int j)
    {
        if (x == word.size())
            return true;
        
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size())
            return false;
        
        bool solved = false;
        
        if (word[x] == board[i][j])
        {
            board[i][j] = '-';
            solved = solve(board, word, x + 1, i + 1, j) || 
                solve(board, word, x + 1, i - 1, j) ||
                solve(board, word, x + 1, i, j - 1) ||
                solve(board, word, x + 1, i, j + 1);
            board[i][j] = word[x];
        }
        return solved;
    }
    
    bool exist(vector<vector<char>>& board, string word) 
    {
        for (int i=0; i<board.size(); i++)
        {
            for (int j=0; j<board[0].size(); j++)
            {
                if (solve(board, word, 0, i, j))
                    return true;
            }
        }
        return false;
    }
};
