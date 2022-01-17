class Solution {
public:
        
    int orangesRotting(vector<vector<int>>& grid) 
    {
        queue<pair<int,int>> q;
        
        int row = grid.size();
        int col = grid[0].size();
        int fresh_count = 0;
        
        for (int i=0; i<row; i++)
        {
            for (int j=0; j<col; j++)
            {
                if (grid[i][j] == 2)
                {
                    q.push({i, j});
                }
                else if (grid[i][j] == 1)
                {
                    fresh_count++;
                }
            }
        }
        
        int t = 0;
        vector<pair<int,int>> adj;
        adj.push_back({-1, 0});
        adj.push_back({0, 1});
        adj.push_back({1, 0}); 
        adj.push_back({0, -1});
        
        while (!q.empty() && fresh_count > 0)
        {
            int len = q.size();
            for (int i=0; i<len; i++)
            {
                int r = q.front().first;
                int c = q.front().second;
                q.pop();
                
                for (int k=0; k<4; k++)
                {
                    int x = r + adj[k].first;
                    int y = c + adj[k].second;
                    
                    if (x < 0 || x > row - 1 || y < 0 || y > col - 1)
                        continue;
                    
                    if (grid[x][y] == 1)
                    {
                        grid[x][y] = 2;
                        q.push({x, y});
                        fresh_count--;
                    }
                }
            }
            t++;
        }
        return fresh_count > 0 ? -1 : t;
    }
};


