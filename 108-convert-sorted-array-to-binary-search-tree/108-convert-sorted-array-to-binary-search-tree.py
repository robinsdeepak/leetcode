# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, nums, start, end):
        if (start > end):
            return None
        elif (start == end):
            return TreeNode(nums[start])
        else:
            mid = (end + start) // 2
            root = TreeNode(nums[mid])
            root.left = self.build(nums, start, mid - 1)
            root.right = self.build(nums, mid + 1, end)
            return root
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums) - 1)
