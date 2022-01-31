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
        
        m = {None:None}
        
        ptr = head
        
        while (ptr):
            tmp = Node(ptr.val)
            m[ptr] = tmp
            ptr = ptr.next
        
        ptr = head
        while (ptr):
            m[ptr].next = m[ptr.next]
            m[ptr].random = m[ptr.random]
            ptr = ptr.next
            
        return m[head]
        