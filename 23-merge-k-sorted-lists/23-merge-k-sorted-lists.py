# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        
        n = len(lists)
        half = n // 2
        
        l1 = lists[:half]
        l2 = lists[half:]
        
        l1 = self.mergeKLists(l1)
        l2 = self.mergeKLists(l2)
        
        merged = ListNode(-1)
        ptr = merged
        i = 0
        j = 0
        
        while (l1 is not None and l2 is not None):
            if (l1.val < l2.val):
                ptr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                ptr.next = ListNode(l2.val)
                l2 = l2.next
            ptr = ptr.next
        
        while (l1 is not None):
            ptr.next = ListNode(l1.val)
            l1 = l1.next
            ptr = ptr.next

        while (l2 is not None):
            ptr.next = ListNode(l2.val)
            l2 = l2.next
            ptr = ptr.next

        return merged.next

