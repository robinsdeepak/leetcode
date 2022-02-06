# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    curr_path = []
    
    def getPath(self, root, target, curr_path):
        if root is None:
            return False
        curr_path.append(root)

        if (root == target):
            return True
        
        if (self.getPath(root.left, target, curr_path) or self.getPath(root.right, target, curr_path)):
            return True
        
        curr_path.pop()
        
        return False
         
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = []
        self.getPath(root, p, p_path)
        q_path = []
        self.getPath(root, q, q_path)
        
        # print([x.val for x in p_path])
        # print([x.val for x in q_path])
        
        c = root
        
        for i in range(min(len(p_path), len(q_path))):
            if (p_path[i] == q_path[i]):
                c = p_path[i]
            else:
                break
        
        return c
