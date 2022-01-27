# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dq = deque([(root, 1)])
        
        max_width = 1    
        while (len(dq)):
            n = len(dq)
            curr_width = dq[-1][1] - dq[0][1] + 1
            max_width = max(curr_width, max_width)
            for i in range(n):
                top = dq[0][0]
                idx = dq[0][1]
                
                dq.popleft()
                if (top.left):
                    dq.append((top.left, idx * 2))
                if (top.right):
                    dq.append((top.right, idx * 2 + 1))
        return max_width
