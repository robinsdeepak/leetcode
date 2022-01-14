class StockSpanner {
public:

    stack<int> st;
    vector<int> prices;
    vector<int> v;
    
    int next(int price) 
    {
        int i = prices.size();
        prices.push_back(price);
        
        while (!st.empty() && prices[st.top()] <= price)
        {
            st.pop();
        }
        int ans;
        
        if (st.empty())
            ans = i + 1;
        else
        {
            ans = i - st.top();
        }
        
        st.push(i);
        return ans;
    }
};


/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */

