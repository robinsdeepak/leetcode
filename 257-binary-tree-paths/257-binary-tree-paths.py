# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = []
    
    def solve(self, root, curr):
        if (root.left is None) and (root.right is None):
            curr.append(root.val)
            self.ans.append("->".join(map(lambda x: str(x), curr)))
            return
        
        if root.left:
            self.solve(root.left, curr + [root.val])
        if root.right:
            self.solve(root.right, curr + [root.val])
        
        
    def binaryTreePaths(self, root):
        self.solve(root, [])
        return self.ans

        