class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> result(grid);
        
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                int x = (n*i+j+k)/n%m;
                int y = (n*i+j+k)%n;
                result[x][y] = grid[i][j];
            }
        }
        
        return result;
    }
};

