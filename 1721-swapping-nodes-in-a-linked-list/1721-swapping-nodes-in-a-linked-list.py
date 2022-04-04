# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        ptr = head
        
        l = []
        
        while ptr:
            l.append(ptr)
            ptr = ptr.next
            
        n = len(l)
        
        l[k - 1], l[n - k] = l[n - k], l[k - 1]
        
        head2 = l[0]
        
        for i in range(1, n):
            l[i - 1].next = l[i]
        
        l[n-1].next = None
        
        return l[0]
