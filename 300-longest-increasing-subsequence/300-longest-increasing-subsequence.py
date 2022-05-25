from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        nxt = [0] * (n + 1)
        cur = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -2, -1):
                ln = nxt[j + 1]
                if j == -1 or nums[i] > nums[j]:
                    ln = max(ln, nxt[i+1] + 1)
                cur[j + 1] = ln
            nxt = cur
        return cur[0]
