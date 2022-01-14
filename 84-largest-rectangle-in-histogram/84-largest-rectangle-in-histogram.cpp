class Solution {
public:
    int largestRectangleArea(vector<int>& heights) 
    {
        int n = heights.size();
        int max_area = -1;
        stack<int> st;
        
        for (int i=0; i<n; i++)
        {
            while (!st.empty() && heights[st.top()] >= heights[i])
            {
                int top = st.top();
                st.pop();
                max_area = max(max_area, heights[top] * (st.empty() ? i : i - st.top() - 1));
            }
            st.push(i);
        }
        while (!st.empty())
        {
            int top = st.top();
            st.pop();
            max_area = max(max_area, heights[top] * (st.empty() ? n : n - st.top() - 1));
        }
        return max_area;
    }
};

