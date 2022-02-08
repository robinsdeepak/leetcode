// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends


int bitCount(int n)
{
    int count = 0;
    while (n)
    {
        count += (n & 1);
        n >>= 1;
    }
    return count;
}

static bool compare(const int a,const int b)
{
    return bitCount(a) > bitCount(b);
}
    
class Solution{
    public:
    void sortBySetBitCount(int arr[], int n)
    {
        stable_sort(arr, arr + n, compare);
    }
};

// { Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        Solution ob;
        ob.sortBySetBitCount(arr, n);
        for (int i = 0; i < n; i++)
            cout << arr[i] << " ";
        cout << endl;
    }
    return 0;
}
  // } Driver Code Ends