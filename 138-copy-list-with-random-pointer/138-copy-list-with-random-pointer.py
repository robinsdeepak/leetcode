"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
                
        ptr = head
        m = {}
        while (ptr):
            tmp = Node(ptr.val)
            m[ptr] = tmp
            ptr = ptr.next
        
        ptr = head
        while (ptr):
            m[ptr].next = m.get(ptr.next)
            m[ptr].random = m.get(ptr.random)
            ptr = ptr.next
            
        return m[head]
        