# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pruneTree(self, root_):
        def solve(root):
            if not root:
                return False

            l = solve(root.left)
            r = solve(root.right)

            if not l:
                root.left = None

            if not r:
                root.right = None


            return root.val == 1 or l or r
        
        x = solve(root_)
        if not x and root_.val == 0:
            return None
        return root_

