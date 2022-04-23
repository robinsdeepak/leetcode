// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution 
{
    public:
    //Function to find minimum time required to rot all oranges. 
    int orangesRotting(vector<vector<int>>& grid) {
    
        int freshCount = 0;
        
        int m = grid.size(), n = grid[0].size();
        
        queue<pair<int,int>> q;
        
        for (int i=0; i<m; i++) 
        {
            for (int j=0; j<n; j++)
            {
                if (grid[i][j] == 1) 
                    freshCount++;
                else if (grid[i][j] == 2)
                    q.push({i, j});
            }
        }
        
        int t = 0;
        
        while (!q.empty())
        {
            int k = q.size();
            t++;
            while (k--)
            {
                pair<int,int> p = q.front();
                q.pop();
                
                int x = p.first, y = p.second;
                vector<pair<int,int>> nbrs = {{x+1,y},{x,y+1},{x-1,y},{x,y-1}};
                
                for (auto p2: nbrs)
                {
                    int i = p2.first, j = p2.second;
                    if (i >= 0 and i < m and j >= 0 and j < n and grid[i][j] == 1) 
                    {
                        freshCount--;
                        if (freshCount == 0) return t;
                        
                        grid[i][j] = 2;
                        q.push({i, j});
                    }
                }
            }
        }
        return freshCount == 0 ? t : -1;
    }
};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m;
		cin >> n >> m;
		vector<vector<int>>grid(n, vector<int>(m, -1));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				cin >> grid[i][j];
			}
		}
		Solution obj;
		int ans = obj.orangesRotting(grid);
		cout << ans << "\n";
	}
	return 0;
}  // } Driver Code Ends