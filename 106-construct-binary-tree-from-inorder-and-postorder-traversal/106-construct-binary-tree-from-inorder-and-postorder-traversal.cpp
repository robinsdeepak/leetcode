
class Solution {
public:
    unordered_map<int, int> m;

    TreeNode *build(vector<int> &postorder, vector<int> &inorder, int &rootIdx, int s, int e)
    {
        if (s > e) return NULL;
        
        int pivot = m[postorder[rootIdx]];
        rootIdx--;
        
        TreeNode *node = new TreeNode(inorder[pivot]);
        
        node->right = build(postorder, inorder, rootIdx, pivot + 1, e);
        node->left = build(postorder, inorder, rootIdx, s, pivot - 1);
        return node;
    }
    
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) 
    {
        int n = postorder.size();
        int rootIdx = n - 1;
        
        for (int i=0; i<n; i++) 
            m[inorder[i]] = i;
        
        return build(postorder, inorder, rootIdx, 0, n - 1);
    }
};
