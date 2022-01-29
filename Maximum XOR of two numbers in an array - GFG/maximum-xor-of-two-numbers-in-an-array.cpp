// { Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function Template for C++

class Solution
{
    public:
    int max_xor(int arr[] , int n)
    {
        
        int mask = 0, mx = 0;
        
        for (int i=31; i>=0; i--)
        {
            mask = mask | (1 << i);
            
            unordered_set<int> s;
            for (int i=0; i<n; i++) s.insert(arr[i] & mask);
            
            int tmp = mx | (1 << i);
            for (int x: s)
            {
                if (s.count(x ^ tmp))
                {
                    mx = tmp;
                    break;
                }
            }
        }
        return mx;
    }
    
};


// { Driver Code Starts.
int main()
{
	int t;
	cin >> t;

	while (t--)
	{
		int n;
		cin >> n;

		int a[n];
		for (int i = 0; i < n; i++)
			cin >> a[i];

        Solution ob;
		cout << ob.max_xor(a, n) << endl;

	}
}


  // } Driver Code Ends