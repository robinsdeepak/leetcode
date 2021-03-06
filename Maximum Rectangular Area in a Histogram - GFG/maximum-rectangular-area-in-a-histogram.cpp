// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution
{
    public:
    //Function to find largest rectangular area possible in a given histogram.
    long long getMaxArea(long long arr[], int n)
    {
        long long max_area = -1;
        stack<int> st;
        int i=0;
        for (; i<n; i++)
        {
            while (!st.empty() && arr[st.top()] >= arr[i])
            {
                int tp = st.top();
                st.pop();
                max_area = max((arr[tp] * (st.empty() ? i : i - st.top() - 1)), max_area);
            }
            st.push(i);
        }
        while (!st.empty())
        {
            int tp = st.top();
            st.pop();
            max_area = max((arr[tp] * (st.empty() ? i : i - st.top() - 1)), max_area);
        }
        return max_area;
    }
};




// { Driver Code Starts.

int main()
 {
    long long t;

    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        
        long long arr[n];
        for(int i=0;i<n;i++)
            cin>>arr[i];
        Solution ob;
        cout<<ob.getMaxArea(arr, n)<<endl;
    
    }
	return 0;
}
  // } Driver Code Ends