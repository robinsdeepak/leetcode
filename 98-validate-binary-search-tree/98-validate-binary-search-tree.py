# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, min_val, max_val):
        if root is None:
            return True
        
        if not (min_val < root.val < max_val):
            return False
        
        return self.solve(root.left, min_val, root.val) and self.solve(root.right, root.val, max_val)
    
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_val = - (2 ** 32)
        max_val = 2 ** 32
        
        return self.solve(root, min_val, max_val)

    