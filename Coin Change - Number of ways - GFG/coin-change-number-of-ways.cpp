// { Driver Code Starts
//Initial Template for C++


#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//User function Template for C++


class Solution
{
    public:
    //Function to find out the number of ways to use the coins to
    
    
    long long solve(vector<vector<int>> &dp, int coins[], int n, int value, int s)
    {
        if (value == 0) return 1;
        if (value < 0) return 0;
        if (dp[value][s] != -1) return dp[value][s];
        
        long long count = 0;
        for (int i=s; i<n; i++)
        {
            count += solve(dp, coins, n, value - coins[i], i);
        }
        // return count;
        return dp[value][s] = count;
    }
    
    long long numberOfWays(int coins[],int n,int v)
    {
        vector<vector<int>> dp(v + 1, vector<int>(n + 1, -1));
        sort(coins, coins + n);
        return solve(dp, coins, n, v, 0);
    }
};


// { Driver Code Starts.


int main() {
    
    //taking total count of testcases
	int testcases;
	cin>>testcases;
	while(testcases--)
	{
	    //taking value
	    int value;
	    cin>>value;
	    
	    //taking number of coins
	    int numberOfCoins;
	    cin>>numberOfCoins;
	    int coins[numberOfCoins];
	    
	    //inserting coins to the array
	    for(int i=0;i<numberOfCoins;i++)
	    cin>>coins[i];
	    Solution obj;
	    //calling function numberOfWays
	    cout<<obj.numberOfWays(coins,numberOfCoins,value)<<endl;
	    
	}
	return 0;
}  // } Driver Code Ends