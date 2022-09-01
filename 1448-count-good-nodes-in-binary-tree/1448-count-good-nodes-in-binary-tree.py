# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def preorder(node, mx):
            if not node:
                return 0
            
            curr_max = max(mx, node.val)
            
            return preorder(node.left, curr_max) + preorder(node.right, curr_max) + (mx <= node.val)
        
        return preorder(root, -inf)
