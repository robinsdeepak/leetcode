class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])

        m = {}
        
        for x in nums:
            diff = rev(x) - x
            if diff not in m:
                m[diff] = 0
            m[diff] += 1

        ans = 0        
        M = 10 ** 9 + 7
        
        for k, v in m.items():
            ans = (ans + (v * (v - 1)) // 2) % M
        return ans
