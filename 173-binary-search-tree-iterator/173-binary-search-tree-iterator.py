# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def pushLefts(root, arr):
    while root:
        arr.append(root)
        root = root.left

class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.index = 0
        pushLefts(root, self.stack)
        
    def next(self) -> int:
        if self.hasNext():
            curr = self.stack[-1]
            self.stack.pop()
            pushLefts(curr.right, self.stack)
            return curr.val
        else:
            return -1
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0

