
class Solution{
    public:
    void find(vector<vector<int>> &m, int n, vector<string> &paths, string curr, int i, int j) 
    {
        if (i < 0 || i >= n || j < 0 || j >= n || m[i][j] == 0)  return;

        if (i == n - 1 && j == n - 1)
        {
            paths.push_back(curr);
            return;
        }
        
        m[i][j] = 0;
        
        find(m, n, paths, curr + "D", i + 1, j);
        find(m, n, paths, curr + "L", i, j - 1);
        find(m, n, paths, curr + "R", i, j + 1);
        find(m, n, paths, curr + "U", i - 1, j); 
        
        m[i][j] = 1;
        
    }
    vector<string> findPath(vector<vector<int>> &m, int n)
    {
        vector<string> paths;
        find(m, n, paths, "", 0, 0);
        sort(paths.begin(), paths.end());
        return paths;
    }
};
