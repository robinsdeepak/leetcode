class Solution:
    def sortedListToBST(self, head):
        if not head: return None
        if not head.next: 
            return TreeNode(head.val)
        if not head.next.next:
            root = TreeNode(head.next.val)
            root.left = TreeNode(head.val)
            return root
        
        fast, slow, prev = head, head, head
        
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            
        root = TreeNode(slow.val)
        prev.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
    
        return root
