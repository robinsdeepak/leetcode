# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        traversal = []
        
        
        q1 = [root]
        
        while len(q1):
            
            q2 = []
            level = []
            
            for node in q1:
                level.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            traversal.append(level)
            q1 = q2
        
        return traversal[::-1]
