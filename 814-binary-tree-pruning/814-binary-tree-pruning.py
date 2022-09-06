# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pruneTree(self, root):
        return self.solution_2(root)
    
    def solution_1(self, root_):
        def solve(root):
            if not root:
                return False

            l = solve(root.left)
            r = solve(root.right)

            if not l:
                root.left = None

            if not r:
                root.right = None

            return root.val or l or r
        
        return root_ if solve(root_) else None

    def solution_2(self, root_):
        def solve(root):
            if not root:
                return None
            root.left = solve(root.left)
            root.right = solve(root.right)
            if not (root.val or root.left or root.right):
                return None
            return root
        return solve(root_)
    