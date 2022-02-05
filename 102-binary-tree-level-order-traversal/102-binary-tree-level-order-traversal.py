# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q1 = [root]
        out = []
        
        while (len(q1)):
            n = len(q1)
            q2 = []
            level = []
            for i in range(n):
                node = q1[i]
                level.append(node.val)
                if (node.left):
                    q2.append(node.left)
                if (node.right):
                    q2.append(node.right)
            q1 = q2
            out.append(level)
        return out
