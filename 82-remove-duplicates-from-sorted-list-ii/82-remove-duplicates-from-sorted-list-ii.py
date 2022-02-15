# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        prev.next = head
        
        ptr = head
        freq = {}
        while (ptr):
            if ptr.val not in freq:
                freq[ptr.val] = 0
            freq[ptr.val] += 1
            ptr = ptr.next

        ptr = prev
        while (ptr.next):
            if (freq[ptr.next.val] > 1):
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        
        return prev.next

        