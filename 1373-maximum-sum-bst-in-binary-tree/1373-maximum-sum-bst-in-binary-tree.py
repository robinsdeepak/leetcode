# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.s = 0
        
        def helper(cur):
            if not cur:
                return (0, float('inf'), float('-inf'))
            
            a, amin, amax = helper(cur.left) 
            b, bmin, bmax = helper(cur.right)
            
            if a is not None and b is not None:
                if cur.val > amax and cur.val < bmin:
                    s = cur.val + a + b
                    self.s = max(self.s, s)
                    return s, min(cur.val, amin), max(cur.val, bmax)
            return (None, None, None)
        
        helper(root)
        
        return self.s
