class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bitcount(n):
            ans = 0
            x = n
            while x:
                if x & 1:
                    ans += 1
                x >>= 1
            return ans, n
        
        arr.sort(key=bitcount)
        
        return arr
