# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, list1, list2):
        if not list1: return list2
        if not list2: return list1
        
        if list1.val < list2.val:
            list1.next = self.merge(list1.next, list2)
            return list1
        else:
            list2.next = self.merge(list1, list2.next)
            return list2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        if not head.next.next:
            l1 = head
            l2 = head.next
            head.next = None
            return self.merge(l1, l2)
        
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        list1 = head
        list2 = slow.next
        slow.next = None
        
        l1 = self.sortList(list1)
        l2 = self.sortList(list2)

        return self.merge(l1, l2)

