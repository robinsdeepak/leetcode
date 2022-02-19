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
    int ans = -1;
    
    void helper(TreeNode *root, int &k)
    {
        if (!root or k == 0) return;
        
        helper(root->left, k);
        k--;
        if (k == 0) ans = root->val;
        helper(root->right, k);
    }
    
    int kthSmallest(TreeNode* root, int k) {
        int K = k;
        helper(root, K);
        return ans;
    }
};

