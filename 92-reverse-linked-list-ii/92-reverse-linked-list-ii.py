# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        nxt = None
        
        while head:
            nxt = head.next
            head.next = None
            if (prev == None):
                prev = head
            else:
                head.next = prev
            
            prev = head
            head = nxt
        
        return prev
        
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        new_head = ListNode(0, head)
        
        count = 0
        
        pre_left = new_head
        while count < left - 1:
            pre_left = pre_left.next
            count += 1
        
        lnode = pre_left.next
        pre_left.next = None
        
        rnode = lnode
        count += 1
        while count < right:
            rnode = rnode.next
            count += 1
        
        post_right = rnode.next
        
        rnode.next = None
        rev = self.reverseList(lnode)
        ptr = rev

        pre_left.next = rnode
        lnode.next = post_right
        
        return new_head.next


