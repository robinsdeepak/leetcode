
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap_ = [-s for s in stones]
        heapq.heapify(heap_)
        
        while len(heap_) > 1:
            x = heapq.heappop(heap_)
            y = heapq.heappop(heap_)
            
            if (x != y):
                heapq.heappush(heap_, x - y)
            
        return -heap_[0] if len(heap_) else 0 
