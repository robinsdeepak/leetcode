class MyStack {
public:
    queue<int> q1;
    queue<int> q2;
    int top_;
    
    MyStack() 
    {

    }
    
    void push(int x) {
        q1.push(x);
        top_ = x;
    }
    
    int pop() {
        int x;
        while (!q1.empty())
        {
            if (q1.size() > 1)
            {
                top_ =  q1.front();
                q2.push(top_);
            }                
            else
            {
                x = q1.front();
            }
            q1.pop();
        }
        swap(q1, q2);
        return x;
    }
    
    int top() {
        return top_;
    }
    
    bool empty() {
        return q1.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */