# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.ans = []
        
        def inorder(node, path):
            if not node:
                return

            path.append(node.val)
            
            if (node.left is None) and (node.right is None):
                # print(sum(path), path)
                if sum(path) == targetSum:
                    self.ans.append(path.copy())
            
            inorder(node.left, path)
            inorder(node.right, path)
            path.pop()
            
            return path
        
        inorder(root, [])
        return self.ans
