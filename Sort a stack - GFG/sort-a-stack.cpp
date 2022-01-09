// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

class SortedStack{
public:
	stack<int> s;
	void sort();
};

void printStack(stack<int> s)
{
    while (!s.empty())
    {
        printf("%d ", s.top());
       	s.pop();
    }
    printf("\n");
}

int main()
{
int t;
cin>>t;
while(t--)
{
	SortedStack *ss = new SortedStack();
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
	int k;
	cin>>k;
	ss->s.push(k);
	}
	ss->sort();
	printStack(ss->s);
}
}// } Driver Code Ends


void SortedStack :: sort()
{
    if(s.empty())
        return;
    
    int temp=s.top();
    s.pop();
    sort();
    
    
    if(!s.empty() && s.top() > temp)
    {
        int t=s.top();
        s.pop();
        s.push(temp);
        sort();
        temp=t;
    }
    s.push(temp);
}

