class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        
        deque<int> q;
        int m = grid.size();
        int n = grid[0].size();
        int t = m * n;
        
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                q.push_back(grid[i][j]);
            }
        }
        
        k = k % t;
        if (k <= t / 2) {
            for (int i=0; i<k; i++) {
                int b = q.back();
                q.pop_back();
                q.push_front(b);
            }
        } else {
            k = t - k;
            for (int i=0; i<k; i++) {
                int f = q.front();
                q.pop_front();
                q.push_back(f);
            }
        }
        
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                grid[i][j] = q.front();
                q.pop_front();
            }
        }
        return grid;
    }
};

