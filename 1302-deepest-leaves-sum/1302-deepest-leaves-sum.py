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
                
        q = [root]
        
        while len(q):
            q2 = set()
            
            for node in q:
                if node.left:  q2.add(node.left)
                if node.right: q2.add(node.right)
            
            if not q2: 
                return sum(map(lambda x: x.val, q))
            
            q = q2
            
        return -1

        