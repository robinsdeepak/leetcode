# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        traversal = defaultdict(list)
        
        q = [(root, 0, 0)]
        
        while len(q):
            
            q2 = []
            
            for node, h, v in q:
                traversal[h].append((node.val, v))
                
                if node.left:
                    q2.append((node.left, h - 1, v + 1))
                    
                if node.right:
                    q2.append((node.right, h + 1, v + 1))
                
            q = q2
        
        ans = []
        for k in sorted(list(traversal.keys())):
            s = sorted(traversal[k], key=lambda x: (x[1], x[0]))
            ans.append([x[0] for x in s])
        return ans
