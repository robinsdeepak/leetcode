# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr = head
        
        while ptr:            
            val = ptr.val
            nextt = ptr
            
            while nextt and val == nextt.val:
                nextt = nextt.next
            ptr.next = nextt
            ptr = ptr.next
            
        return head
