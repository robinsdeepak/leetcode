# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    m = {None: 0}
    
    def calculatePathSum(self, root):
        if root is None:
            return 0
        
        self.m[root] = root.val + max(0, self.calculatePathSum(root.left), self.calculatePathSum(root.right))
        return self.m[root]
    
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        self.calculatePathSum(root)
        
        q1 = [root]
        max_path_sum = root.val
        
        while (len(q1)):
            n = len(q1)
            q2 = []
            for i in range(n):
                node = q1[i]
                
                max_path_sum = max(
                    node.val,
                    node.val + self.m[node.left],
                    node.val + self.m[node.right],
                    node.val + self.m[node.left] + self.m[node.right],
                    max_path_sum
                )
                
                if (node.left):
                    q2.append(node.left)
                if (node.right):
                    q2.append(node.right)
                
            q1 = q2
        
        return max_path_sum

