# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(root, arr):
    if not root:
        return
    inorder(root.left, arr)
    arr.append(root.val)
    inorder(root.right, arr)

class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        inorder(root, self.arr)
        self.index = 0

    def next(self) -> int:
        if self.hasNext():
            self.index += 1
            return self.arr[self.index - 1]
        else:
            return -1
    
    def hasNext(self) -> bool:
        return self.index < len(self.arr)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()