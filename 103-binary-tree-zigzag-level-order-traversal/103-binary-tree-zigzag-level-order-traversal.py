# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q1 = [root]
        ans = []
        rev = False
        
        while (len(q1)):
            if rev:
                ans.append(reversed([node.val for node in q1]))
            else:
                ans.append([node.val for node in q1])
            
            rev = not rev
            
            q2 = []
            for node in q1:
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            q1 = q2
            
        return ans
