// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
/*
The structure of the class is as follows
class _stack{
stack<int> s;
int minEle;
public :
    int getMin();
    int pop();
    void push(int);
};
*/

class Solution
{
    int min_el;
    stack<int> st;
    public:
    
       /*returns min element from stack*/
       int getMin()
       {   
            if (st.empty())
                return -1;
            return min_el;
       }
       
       /*returns poped element from stack*/
       int pop()
       {
           if (st.empty())
                return -1;
                
           int top = st.top() < min_el ? min_el : st.top();
            if (st.top() < min_el)
                min_el = 2 * min_el - st.top();   
            st.pop();
            return top;
       }
       
       /*push element x into the stack*/
       void push(int val)
       {
            if (st.empty())
            {
                st.push(val);
                min_el = val;
            }
            else if (val >= min_el)
            {
                st.push(val);
            }
            else
            {
                st.push(2 * val - min_el);
                min_el = val;
            }
       }
};

// { Driver Code Starts.

int main()
 {
    long long t;

    cin>>t;
    while(t--)
    {
        int q;
        cin>>q;
        Solution ob;
        while(q--){
           int qt;
           cin>>qt;
           if(qt==1)
           {
              //push
              int att;
              cin>>att;
              ob.push(att);
           }
           else if(qt==2)
           {
              //pop
              cout<<ob.pop()<<" ";
           }
           else if(qt==3)
           {
              //getMin
              cout<<ob.getMin()<<" ";
           }
       }
       cout<<endl;
    }
    return 0;
}
  // } Driver Code Ends