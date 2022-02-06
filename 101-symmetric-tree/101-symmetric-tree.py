# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def solve(self, left, right):
        if (left is None) or (right is None):
            return not ((left is None) ^ (right is None))
        
        if (left.val != right.val):
            return False
        
        if not (self.solve(left.left, right.right) and self.solve(left.right, right.left)):
            return False
        
        return True
        
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        return self.solve(root.left, root.right)
