// { Driver Code Starts
/* program to construct tree using inorder and postorder traversals */
#include <bits/stdc++.h>
using namespace std;

/* A binary tree node has data, pointer to left child
   and a pointer to right child */
struct Node {
    int data;
    struct Node* left;
    struct Node* right;

    Node(int x) {
        data = x;
        left = right = NULL;
    }
};

/* This funtcion is here just to test buildTreeUtil() */
void preOrder(Node* node) {
    if (node == NULL) return;

    /* then print the data of node */
    printf("%d ", node->data);

    /* first recur on left child */
    preOrder(node->left);

    /* now recur on right child */
    preOrder(node->right);
}

Node* buildTree(int in[], int post[], int n);

int main() {
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        int in[n], post[n];
        for (int i = 0; i < n; i++) cin >> in[i];
        for (int i = 0; i < n; i++) cin >> post[i];
        Node* root = buildTree(in, post, n);
        preOrder(root);
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends


/* Tree node structure

struct Node
{
    int data;
    struct Node* left;
    struct Node* right;

    Node(int x)
    {
        data = x;
        left = right = NULL;
    }
};

*/

unordered_map<int,int> m;

Node *buildUtil(int in[], int post[], int inStrt, int inEnd, int *pIndex)
{
    if (inStrt > inEnd)
        return NULL;

    Node *node = new Node(post[*pIndex]);
    (*pIndex)--;

    if (inStrt == inEnd)
        return node;

    int iIndex = m[node->data];

    node->right = buildUtil(in, post, iIndex + 1, inEnd, pIndex);
    node->left = buildUtil(in, post, inStrt, iIndex - 1, pIndex);

    return node;
}


//Function to return a tree created from postorder and inoreder traversals.
Node *buildTree(int in[], int post[], int n) 
{
    for (int i=0; i<n; i++)
        m[in[i]] = i;
    
    int pIndex = n - 1;
    
    return buildUtil(in, post, 0, n - 1, &pIndex);
}


