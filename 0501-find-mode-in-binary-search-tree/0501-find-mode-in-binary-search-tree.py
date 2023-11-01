# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        
        q = [root]
        
        while len(q):
            q2 = []
            for node in q:
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
                
                freq[node.val] += 1
            q = q2
        
        max_ = max(freq.values())
        
        return [k for k, v in freq.items() if v == max_]
