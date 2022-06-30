# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = 0
        q = [root]
        
        while len(q):
            ans += len(q)
            q2 = []
            
            for node in q:
                
                if node.left: q2.append(node.left)
                if node.right: q2.append(node.right)
            
            q = q2
            
        return ans
