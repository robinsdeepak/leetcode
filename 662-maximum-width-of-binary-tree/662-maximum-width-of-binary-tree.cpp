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
    int widthOfBinaryTree(TreeNode* root) 
    {
        deque<pair<TreeNode*,unsigned long long int>> dq;
        dq.push_back({root,0});
        int max_width = 1;
        while (!dq.empty())
        {
            int n = dq.size();
            int curr_width = int(dq.back().second - dq.front().second + 1);
            max_width = max(max_width, curr_width);
            while (n--)
            {
                TreeNode *top = dq.front().first;
                unsigned long long int index = dq.front().second;
                dq.pop_front();
                if (top->left)
                    dq.push_back({top->left, 2 * index + 1});
                if (top->right)
                    dq.push_back({top->right, 2 * index + 2});            
            }
        }
        return max_width;
    }
};
