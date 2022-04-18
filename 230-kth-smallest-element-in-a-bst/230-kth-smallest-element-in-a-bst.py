# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ans = -1
        
        def inorder(node):
            if not node:
                return
            
            nonlocal k
            
            if k >= 0:
                inorder(node.left)
                k -= 1
                nonlocal ans
                if k == 0: ans = node.val
                # print(ans, k)
                inorder(node.right)
        
        inorder(root)
        return ans
