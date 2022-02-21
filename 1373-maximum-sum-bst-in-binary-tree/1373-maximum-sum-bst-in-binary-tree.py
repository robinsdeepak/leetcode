# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

MAX = float('inf')
MIN = float('-inf')


class Solution:
    
    def helper(self, root):
        if not root:
            return (0, MAX, MIN)

        a, amin, amax = self.helper(root.left)
        b, bmin, bmax = self.helper(root.right)

        if a is not None and b is not None:
            if amax < root.val < bmin:
                s = a + b + root.val
                self.ans = max(self.ans, s)
                return (s, min(amin, root.val), max(bmax, root.val))
        return (None, None, None)
    
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.helper(root)
        return self.ans
