# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    
    def inorder(self, root):
        if not root: 
            return
        
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.inorder(root1)
        self.inorder(root2)
        return sorted(self.arr)
    