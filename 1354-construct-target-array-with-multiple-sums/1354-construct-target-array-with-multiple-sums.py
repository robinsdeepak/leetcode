from heapq import *

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        hp = [-x for x in target]
        
        heapify(hp)
        total = sum(target)
        
        while True:
            x = -heappop(hp)
            total -= x
            
            if x == 1 or total == 1: 
                return True
            
            if x < total or total == 0 or x % total == 0:
                return False
            
            x %= total
            total += x
            
            heappush(hp, -x)
        
