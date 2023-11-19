from collections import Counter


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        ans = 0
        i = 0
        
        for k, v in sorted(cnt.items(), key=lambda x: x[0]):
            ans += (i * v)
            i += 1
        
        return ans

