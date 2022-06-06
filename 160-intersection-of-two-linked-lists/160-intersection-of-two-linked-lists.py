# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1, head2):
        h1, h2 = head1, head2
        n1, n2 = 0, 0
        
        while h1:
            h1 = h1.next
            n1 += 1
        
        while h2:
            h2 = h2.next
            n2 += 1
        
        if n1 < n2:
            h1, h2 = head2, head1
            n1, n2 = n2, n1
        else:
            h1, h2 = head1, head2
        
        diff = n1 - n2
        
        while diff:
            h1 = h1.next
            diff -= 1
        
        while h1 and h2:
            if h1 == h2:
                return h1
            h1 = h1.next
            h2 = h2.next
        
        return None
