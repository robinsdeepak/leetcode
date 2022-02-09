# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def find(self, root, val):
        while root:
            if (root.val == val):
                return root
            root = root.left if val < root.val else root.right
        return None

    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q1 = [root]
        
        while len(q1):
            q2 = []
            for node in q1:
                node2 = self.find(root, k - node.val)
                if (node2 and node2 != node):
                    return True
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            q1 = q2
        return False
