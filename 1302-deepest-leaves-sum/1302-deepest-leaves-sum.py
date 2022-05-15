# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = 0
        
        q = [root]
        
        while len(q):
            q2 = set()
            sm = 0
            
            for node in q:
                sm += node.val
                
                if node.left:  q2.add(node.left)
                if node.right: q2.add(node.right)
            
            q = q2
            ans = sm
        
        return ans

        