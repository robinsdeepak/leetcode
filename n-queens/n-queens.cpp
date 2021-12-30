class Solution {
public:
    map<int,unordered_set<int>> m;
    
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
    
    bool solve(vector<vector<string>> &res, vector<string> s, int n, int x, int y)
    {
        if (y >= n)
        {
            res.push_back(s);
            return true;
        }
        
        for (int i=0; i<n; i++)
        {
            if (isSafe(s, i, y))
            {
                s[i][y] = 'Q';
                if (!solve(res, s, n, x, y + 1))
                {
                    s[i][y] = '.';
                }
                
            }
        }
        return false;
    }
    
    vector<vector<string>> solveNQueens(int n) 
    {
        vector<vector<string>> res;
        vector<string> s(n, string(n, '.'));
        solve(res, s, n, 0, 0);
        return res;
    }
};


