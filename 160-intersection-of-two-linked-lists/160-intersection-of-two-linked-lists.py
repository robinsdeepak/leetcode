# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1, head2):
        return self.solution_2(head1, head2)
    
    def solution_1(self, head1, head2):
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

    def solution_2(self, head1, head2):
        st1, st2 = [], []
        h1, h2 = head1, head2
        
        while h1:
            st1.append(h1)
            h1 = h1.next
        
        while h2:
            st2.append(h2)
            h2 = h2.next
        
        prev = None
        while st1 and st2:
            h1, h2 = st1.pop(), st2.pop()
            if h1 != h2:
                return prev
            prev = h1
        
        return prev
