# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    m = {}
    ans = 0
    
    def height(self, root):
        if (root is None):
            return 0
        self.m[root] = 1 + max(self.height(root.left), self.height(root.right))
        return self.m[root]
    
    def solve(self, root):
        if (root is None):
            return 0
        
        return max(self.m[root.left] + self.m[root.right], 
                   self.solve(root.left), self.solve(root.right))
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.m[None] = 0
        self.height(root)
        return self.solve(root)
