class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def cost(x, s, e):
            return sum(map(lambda y: abs(x - nums[y]), range(s, e + 1)))
        
        nums.sort()
        
        n = len(nums)
        l, h = 0, n - 1
        
        ans = float('inf')
        
        while l <= h:
            m = (l + h) // 2
            c1 = cost(nums[m], 0, m)
            c2 = cost(nums[m], m + 1, n - 1)
            
            ans = min(ans, c1 + c2)
            
            if c1 < c2:
                l = m + 1
            else:
                h = m - 1
            
        return ans

