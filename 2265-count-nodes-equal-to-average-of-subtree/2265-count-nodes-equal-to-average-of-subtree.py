# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def rec(node):
            if not node:
                return [0, 0]
            
            l = rec(node.left)
            r = rec(node.right)
            
            s = l[0] + r[0] + node.val
            c = l[1] + r[1] + 1
            
            avg = s // c
            
            if avg == node.val:
                self.ans += 1
            
            return [s, c]

        rec(root)
        return self.ans

