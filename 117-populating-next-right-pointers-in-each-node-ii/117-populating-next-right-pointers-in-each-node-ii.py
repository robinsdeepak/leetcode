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
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        
        q = [root]
        
        while len(q):
            q2 = []
            for i in range(len(q) - 1):
                node = q[i]
                node.next = q[i + 1]
                
                if node.left: q2.append(node.left)
                if node.right: q2.append(node.right)
                    
            node = q[len(q) - 1]
            if node.left: q2.append(node.left)
            if node.right: q2.append(node.right)
            q = q2
        
        return root
