from functools import lru_cache

class Solution:
        
    def furthestBuilding(self, H: List[int], bricks: int, ladders: int) -> int:
        n = len(H)
        jumps_pq = []
        for i in range(n - 1):
            jump_height = H[i + 1] - H[i]
            if jump_height <= 0: continue
            
            heappush(jumps_pq, jump_height)
            
            if len(jumps_pq) > ladders:
                bricks -= heappop(jumps_pq)
            
            if bricks < 0: return i
        
        return n - 1
