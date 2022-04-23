// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function Template for C++

class Solution
{
    public:
    int searchInsertK(vector<int>arr, int n, int k)
    {
        int l = 0;
        int h = n - 1;
        
        while (l <= h) 
        {
            // cout << l << " " << h << endl;
            int mid = l + (h - l) / 2;
            if (arr[mid] == k) return mid;
            
            if (mid == 0 && arr[mid] > k) return 0;
            if (mid == n - 1 && arr[mid] < k) return n;
            
            if (arr[mid] < k && arr[mid + 1] > k) return mid + 1;
            if (arr[mid] > k && arr[mid - 1] < k) return mid;
            
            if (arr[mid] > k) 
                h = mid - 1;
            else
                l = mid + 1;
        }
        return -1;
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin >> N;
        vector<int>Arr(N);
        for(int i=0;i<N;i++)    
            cin>>Arr[i];
        int k;
        cin>>k;
        Solution obj;
        cout<<obj.searchInsertK(Arr, N, k)<<endl;
    }
    return 0;
}  // } Driver Code Ends