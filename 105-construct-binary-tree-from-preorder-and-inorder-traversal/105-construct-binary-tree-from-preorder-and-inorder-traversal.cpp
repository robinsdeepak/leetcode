class Solution 
{
public:
    unordered_map<int, int> m;

    TreeNode *build(vector<int> &preorder, vector<int> &inorder, int &rootIdx, int s, int e)
    {
        if (s > e) return NULL;
        
        int pivot = m[preorder[rootIdx]];
        rootIdx++;
        
        TreeNode *node = new TreeNode(inorder[pivot]);
        
        node->left = build(preorder, inorder, rootIdx, s, pivot - 1);
        node->right = build(preorder, inorder, rootIdx, pivot + 1, e);
        return node;
    }
    
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) 
    {
        int rootIdx = 0;
        int n = preorder.size();
        
        for (int i=0; i<n; i++) 
            m[inorder[i]] = i;
        
        return build(preorder, inorder, rootIdx, 0, n - 1);
    }
};
