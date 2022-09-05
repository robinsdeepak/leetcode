"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        l = [root]
        ans = []
        
        while len(l):
            ln = []
            cl = []
            for node in l:
                cl.append(node.val)
                
                if not node.children:
                    continue
                    
                for ch in node.children:
                    if ch:
                        ln.append(ch)
            
            ans.append(cl)
            l = ln
        
        return ans
