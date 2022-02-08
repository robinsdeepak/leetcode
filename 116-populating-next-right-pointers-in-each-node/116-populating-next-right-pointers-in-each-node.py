"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        q1 = [root]
        
        while (len(q1)):
            n = len(q1)
            q2 = []
            
            for i in range(n):
                node = q1[i]
                if i < n - 1:
                    node.next = q1[i+1]
                
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right) 
            q1 = q2
        
        return root


