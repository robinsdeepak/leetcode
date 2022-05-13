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
        
        curr = root
        prevChild = None
        firstChild = None
        
        while curr:
            
            items = []
            if prevChild: items.append(prevChild)
            if curr.left: items.append(curr.left)
            if curr.right: items.append(curr.right)
            
            for i in range(len(items) - 1):
                items[i].next = items[i + 1]
            
            if items:
                prevChild = items[-1]
            
            if not firstChild and len(items):
                firstChild = items[0]
            
            if curr.next:
                curr = curr.next
            else:
                curr, firstChild, prevChild = firstChild, None, None
                     
        return root
