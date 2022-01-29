// { Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function Template for C++


    void printv(string s, vector<int> v)
    {
        cout << s << ": ";
        for (int x: v)
            cout << x << ", ";
        cout << endl;
    }
    
    
class Solution{
public:
    bool isSafe(vector<int> &board, int n, int x, int y)
    {
        for (int i=0; i<n; i++)
        {
            if (board[i] == y)
            {
                return false;
            }
        }
        
        board[x] = y;
        for (int i=0; i<n; i++)
        {
            for (int j=i+1; j<n; j++)
            {
                if (board[i] != -1 && board[j] != -1 && abs(board[i] - board[j]) == j - i)
                {
                    board[x] = -1;
                    return false;
                }
            }
        }

        return true;
    }

    void solve(vector<vector<int>> &ans, vector<int> &board, int n, int x)
    {
        if (x == n)
        {
            vector<int> tmp;
            for (int z: board)
                tmp.push_back(z + 1);
            ans.push_back(tmp);
            return;
        }
        
        for (int i=0; i<n; i++)
        {
            bool safe = isSafe(board, n, x, i);

            if (safe)
            {
                board[x] = i;
                solve(ans, board, n, x + 1);
                board[x] = -1;
            }
        }
    }

    vector<vector<int>> nQueen(int n) 
    {
        vector<vector<int>> ans;
        vector<int> board(n, -1);
        solve(ans, board, n, 0);
        return ans;
    }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        
        Solution ob;
        vector<vector<int>> ans = ob.nQueen(n);
        if(ans.size() == 0)
            cout<<-1<<"\n";
        else {
            for(int i = 0;i < ans.size();i++){
                cout<<"[";
                for(int u: ans[i])
                    cout<<u<<" ";
                cout<<"] ";
            }
            cout<<endl;
        }
    }
    return 0;
}  // } Driver Code Ends