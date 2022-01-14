class Solution {
public:
    int largestRectangleArea(vector<int>& arr) 
    {
        int n = arr.size();
        int max_area = -1;
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