# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.solution_2(root)
    
    def solution_1(self, root):
        def preorder(node, mx):
            if not node:
                return 0
            
            curr_max = max(mx, node.val)
            
            return preorder(node.left, curr_max) + preorder(node.right, curr_max) + (mx <= node.val)
        
        return preorder(root, -inf)

    def solution_2(self, root):
        q = [(root, -inf)]
        
        ans = 0
        
        while len(q):
            q2 = []
            
            for node, mx in q:
                if node.val >= mx:
                    ans += 1
                
                if node.left:
                    q.append((node.left,  max(mx, node.val)))
                if node.right:
                    q.append((node.right, max(mx, node.val)))
            
            q = q2
        
        return ans

