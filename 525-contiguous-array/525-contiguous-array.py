class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        m = {}
        n = len(nums)
        count = 0
        max_len = 0
        m[0] = -1
        for i in range(n):
            count += (1 if nums[i] else -1)
            if count in m:
                max_len = max(max_len, i - m[count])
            else:
                m[count] = i
        return max_len
