// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends

class Solution
{
    public:
    //Function to find maximum of minimums of every window size.
    vector <int> maxOfMin(int arr[], int n)
    {
        // vector<int> left(n, -1);
        // vector<int> right(n, -1);
        
        // stack<int> st;
        
        // for (int i=0; i<n; i++)
        // {
        //     while (!st.empty() && arr[st.top()] >= arr[i])
        //         st.pop();
                
        //     if (!st.empty()) 
        //         left[i] = st.top();

        //     st.push(i);
        // }
        // while(!st.empty())
        //     st.pop();
            
        // for (int i=n-1; i>=0; i--)
        // {
        //     if (!st.empty() && arr[st.top()] >= arr[i])
        //         st.pop();

        //     if (!st.empty())
        //         right[i] = st.top();
            
        //     st.push(i);
        // }
        
        // vector<int> ans(n, 0);
        
        // for (int i=0; i<n; i++)
        // {
        //     int len = right[i] - left[i] -1;
            
        //     ans[len] = max(arr[i], ans[len]);
        // }
        
        // for (int i=n-1; i>=1; i--)
        //     ans[i] = max(ans[i], ans[i+1]);
        
        // vector<int> v;
        // for (int i: ans) {
        //     // if (i != 0) {
        //         v.push_back(i);
        //     // }
        // }
        // return v;
            stack<int> s; 

    // Arrays to store previous and next smaller
    int left[n+1];  
    int right[n+1]; 

    // Initialize elements of left[] and right[]
    for (int i=0; i<n; i++)
    {
        left[i] = -1;
        right[i] = n;
    }

    // Fill elements of left[] using logic discussed on
    // https://www.geeksforgeeks.org/next-greater-element/
    for (int i=0; i<n; i++)
    {
        while (!s.empty() && arr[s.top()] >= arr[i])
            s.pop();

        if (!s.empty())
            left[i] = s.top();

        s.push(i);
    }

    // Empty the stack as stack is 
// going to be used for right[]
    while (!s.empty())
        s.pop();

    // Fill elements of right[] using same logic
    for (int i = n-1 ; i>=0 ; i-- )
    {
        while (!s.empty() && arr[s.top()] >= arr[i])
            s.pop();

        if(!s.empty())
            right[i] = s.top();

        s.push(i);
    }

    // Create and initialize answer array
    vector<int> ans(n+1, 0);

    // Fill answer array by comparing minimums of all
    // lengths computed using left[] and right[]
    for (int i=0; i<n; i++)
    {
        // length of the interval
        int len = right[i] - left[i] - 1;

        // arr[i] is a possible answer for this length 
        // 'len' interval, check if arr[i] is more than
        // max for 'len'
        ans[len] = max(ans[len], arr[i]);
    }

    // Some entries in ans[] may not be filled yet. Fill 
    // them by taking values from right side of ans[]
    for (int i=n-1; i>=1; i--)
        ans[i] = max(ans[i], ans[i+1]);

    vector<int> v;
    for (auto x: ans)
    {
        if (x)
            v.push_back(x);
    }
    return v;
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++) cin >> a[i];
        Solution ob;
        vector <int> res = ob.maxOfMin(a, n);
        for (int i : res) cout << i << " ";
        cout << endl;
    }
    return 0;
}
  // } Driver Code Ends