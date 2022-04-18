class Solution:
    
    def canReach(self, arr: List[int], start: int) -> bool:
        m = {}
        
        def rec(i):
            if not 0 <= i < len(arr):
                return False
            
            if i in m: return m[i]
            
            m[i] = arr[i] == 0
            
            return m[i] or rec(i - arr[i]) or rec(i + arr[i])
        
        return rec(start)
