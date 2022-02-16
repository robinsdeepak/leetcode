# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, list1, list2):
        if not list1: return list2
        if not list2: return list1
        
        prev = ListNode(0)
        ptr = prev
        while list1 and list2:
            if list1.val <= list2.val:
                ptr.next = list1
                list1 = list1.next
                ptr.next.next = None
                ptr = ptr.next
            else:
                list1, list2 = list2, list1
                
        ptr.next = list1 if list1 else list2
        
        return prev.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow = head
        if head.next.next:
            fast = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
        
        list1 = head
        list2 = slow.next
        slow.next = None
        
        l1 = self.sortList(list1)
        l2 = self.sortList(list2)

        return self.merge(l1, l2)

