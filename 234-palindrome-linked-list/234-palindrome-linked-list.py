# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        
        node = head
        
        for i in range(n // 2 - 1):
            node = node.next
        
        p1 = head
        p2 = node.next
        
        if n & 1:
            p2 = p2.next
        
        node.next = None
        
        p2 = self.reverse(p2)
        
        # self.printList(p1)
        # self.printList(p2)
        
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        
        return True
        
    def reverse(self, head):
        node = None
        while head:
            temp = head
            head = head.next
            temp.next = node
            node = temp
        
        return node

    
    def printList(self, head):
        while head:
            print(head.val, end=', ')
            head = head.next
        print()
        