/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    unordered_map<TreeNode *,int> m;
    
    int height(TreeNode* root)
    {
        if (!root) return 0;
        if (m.count(root)) return m[root];
        
        return m[root] = 1 + max(height(root->left), height(root->right));
    }
    
    bool solve(TreeNode *root)
    {
        if (!root) return true;
        return abs(m[root->left] - m[root->right]) <= 1 && solve(root->left) && solve(root->right);
    }
    
    bool isBalanced(TreeNode* root) 
    {
        height(root);
        return solve(root);
    }
};
