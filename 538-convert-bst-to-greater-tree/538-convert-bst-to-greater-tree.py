# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.curr = 0

        def postorder(root):
            if not root:
                return 0
            postorder(root.right)
            self.curr = self.curr + root.val
            root.val = self.curr
            postorder(root.left)
        
        postorder(root)
        
        return root

