# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        arr = []
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            nonlocal arr
            arr.append(node)
            inorder(node.right)
        
        inorder(root)
        
        for i in range(1, len(arr)):
            arr[i - 1].right = arr[i]
            arr[i - 1].left = None
        
        arr[-1].right = None
        arr[-1].left = None
        
        return arr[0]
