from collections import defaultdict
from heapq import *

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        pq = []
        
        for char, count in freq.items():
            heappush(pq, -count)
        
        ans = 0

        while len(pq) > 1:
            top = -heappop(pq)
            if top == -pq[0]:
                if top > 1:
                    heappush(pq, - (top - 1))
                ans += 1
        return ans
