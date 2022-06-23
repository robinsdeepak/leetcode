from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = []
        for x in nums:
            heappush(s, x)
            
            if len(s) > k:
                heappop(s)
            
        return heappop(s)
