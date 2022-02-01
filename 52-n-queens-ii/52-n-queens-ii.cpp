class Solution {
public:
    
    bool isSafe(vector<string> &s, int x, int y)
    {
        int i, j;
        for (i=0; i<y; i++)
            if (s[x][i] == 'Q')
                return false;
        
        for (i=x, j=y; j>=0 && i>=0; i--, j--)
            if (s[i][j] == 'Q')
                return false;
        
        for (i=x, j=y; j>=0 && i<s.size(); i++, j--)
            if (s[i][j] == 'Q')
                return false;
        
        return true;
    }
    
    bool solve(int &res, vector<string> s, int n, int y)
    {
        if (y >= n)
        {
            res++;
            return true;
        }
        
        for (int x=0; x<n; x++)
        {
            if (isSafe(s, x, y))
            {
                s[x][y] = 'Q';
                if (!solve(res, s, n, y + 1))
                {
                    s[x][y] = '.';
                }
            }
        }
        return false;
    }
    
    int totalNQueens(int n) {
        int res=0;
        vector<string> s(n, string(n, '.'));
        solve(res, s, n, 0);
        return res;
    }
};
