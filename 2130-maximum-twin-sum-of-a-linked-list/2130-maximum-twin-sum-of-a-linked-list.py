# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node1, node2 = head, head
        prev = node1
        while node2 and node2.next:
            prev = node1
            node1 = node1.next
            node2 = node2.next.next

        prev.next = None
        node2 = self.reverse(node1)
        node1 = head

        ans = 0
        
        while node2 and node1:
            ans = max(ans, node1.val + node2.val)
            node1, node2 = node1.next, node2.next
            
        return ans
        
    def reverse(self, head):
        if not head:
            return head
        
        prev = head
        next_ = head.next
        prev.next = None
        
        while next_:
            node = next_
            next_ = node.next
            
            node.next = prev
            prev = node
            
        return prev
