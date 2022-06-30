# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def leftHeight(node):
            x = 0
            while node:
                x += 1
                node = node.left
            return x
        
        def rightHeight(node):
            x = 0
            while node:
                x += 1
                node = node.right
            return x
        
        def rec(node):
            if not node:
                return 0
            
            lh = leftHeight(node)
            rh = rightHeight(node)
            
            if lh == rh:
                return 2 ** lh - 1
            else:
                return 1 + rec(node.left) + rec(node.right)
        
        return rec(root)
    