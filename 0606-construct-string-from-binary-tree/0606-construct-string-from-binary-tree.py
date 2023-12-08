# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def rec(node):
            if node is None:
                return ""
            ans = str(node.val)
            l = rec(node.left)
            r = rec(node.right)
            if l:
                ans += f"({l})"
            if r:
                if not l:
                    ans += "()"
                ans += f"({r})"
            return ans
        
        return rec(root)
