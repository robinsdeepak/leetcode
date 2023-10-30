class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bitcount(n):
            return n.bit_count(), n
        
        arr.sort(key=bitcount)
        
        return arr
