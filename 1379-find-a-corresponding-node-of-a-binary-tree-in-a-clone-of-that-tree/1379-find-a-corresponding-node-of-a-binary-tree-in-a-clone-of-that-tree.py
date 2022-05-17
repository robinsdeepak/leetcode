# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        q = [(original, cloned)]
        
        
        while len(q):
            q2 = []
            
            for n1, n2 in q:
                
                if n1 == target:
                    return n2
                
                if n1.left:
                    q2.append((n1.left, n2.left))
                
                if n1.right:
                    q2.append((n1.right, n2.right))
            
            q = q2
        
        