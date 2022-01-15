class MinStack 
{
public:
    MinStack() 
    {

    }
            stack<int> st;
        vector<int> v;
    void push(int val) 
    {
        st.push(val);
        v.push_back(val);
    }
    
    void pop() 
    {
        st.pop();
        v.pop_back();
    }
    
    int top() 
    {
        return st.top();
    }
    
    int getMin() 
    {
        int minstack = INT_MAX;
        for (auto x: v)
            minstack = min(minstack, x);
        return minstack;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */