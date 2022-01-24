class Solution {
public:
    int max_area = 0;
    int solve(vector<vector<int>>& grid,vector<vector<int>>& v, int x, int y)
    {
        int m = grid.size();
        int n = grid[0].size();
        if (x < 0 || x >= m || y < 0 || y >= n || v[x][y] || !grid[x][y])
        {
            return 0;
        }
        
        v[x][y] = 1;
        
        return 1 + solve(grid, v, x + 1, y) + 
            solve(grid, v, x, y + 1) + 
            solve(grid, v, x - 1, y) + 
            solve(grid, v, x, y - 1);
    }
    
    int maxAreaOfIsland(vector<vector<int>>& grid) 
    {   
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> v(m, vector<int>(n, 0));
        for (int i=0; i<m; i++)
        {
            for (int j=0; j<n; j++)
            {
                max_area = max(max_area, solve(grid, v, i, j));
            }
        }
        return max_area;
    }
};
