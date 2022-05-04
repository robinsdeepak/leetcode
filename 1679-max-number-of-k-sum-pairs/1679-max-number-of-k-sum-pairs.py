class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        
        ans = 0
        for x in freq:
            if x == k - x:
                ans += freq[x] // 2
            else:
                ans += min(freq.get(x, 0), freq.get(k - x, 0))
                if k - x in freq: freq[k - x] = 0
            freq[x] = 0
        return ans
