# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode(0)
        lptr = left
        right = ListNode(0)
        rptr = right
        
        while head:
            nxt = head.next
            head.next = None
            if head.val < x:
                lptr.next = head
                lptr = lptr.next
            else:
                rptr.next = head
                rptr = rptr.next
            head = nxt
        lptr.next = right.next
        return left.next
