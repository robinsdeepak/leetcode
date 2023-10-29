class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        t = (minutesToTest / minutesToDie) + 1
        
        p = 0
        
        while t ** p < buckets:
            p += 1
        
        return p
