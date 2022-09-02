# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        ans = []
        
        q = [root]
        while len(q):
            q2 = []
            s = 0
            for node in q:
                s += node.val
                if node.left: q2.append(node.left)                
                if node.right: q2.append(node.right)
            
            avg = round(s / len(q), 5)
            ans.append(avg)
        
            q = q2
        
        return ans
