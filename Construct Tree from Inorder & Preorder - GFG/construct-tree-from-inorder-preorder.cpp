// { Driver Code Starts
//

#include<bits/stdc++.h>
using namespace std;

struct Node
{
	int data;
	struct Node *left;
	struct Node *right;
	
	Node(int x){
	    data = x;
	    left = NULL;
	    right = NULL;
	}
};


void printPostOrder(Node *root)
{
	if(root==NULL)
		return;
	printPostOrder(root->left);
	printPostOrder(root->right);
	cout<<root->data<<" ";
}

 // } Driver Code Ends


/*Complete the code here.
Node is as follows:
struct Node
{
  int data;
  Node* left;
  Node* right;
};
*/
class Solution{
    public:
    unordered_map<int,int> m;
    
    Node *build(int in[], int pre[], int n, int s, int e, int &rootIdx)
    {
        if (s > e) return NULL;
        
        int pivot = m[pre[rootIdx++]];
        
        Node *node = new Node(in[pivot]);
        
        
        node->left = build(in, pre, n, s, pivot - 1, rootIdx);
        node->right = build(in, pre, n, pivot + 1, e, rootIdx);
        
        return node;
    }
    
    Node* buildTree(int in[],int pre[], int n)
    {
        int rootIdx = 0;
        for (int i=0; i<n; i++)
            m[in[i]] = i;
        return build(in, pre, n, 0, n - 1, rootIdx);
    }
};

// { Driver Code Starts.
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		
		int inorder[n], preorder[n];
		for(int i=0; i<n; i++)
			cin>> inorder[i];
		for(int i=0; i<n; i++)
			cin>> preorder[i];
		Solution obj;
		Node *root = obj.buildTree(inorder, preorder, n);
		printPostOrder(root);
		cout<< endl;
	}
}
  // } Driver Code Ends