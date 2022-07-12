class Solution:
    def makesquare(self, ms: List[int]) -> bool:
        s = sum(ms)
        
        if s % 4: return False
        
        l = s // 4
        
        sides = [0, 0, 0, 0]
        
        ms.sort(reverse=True)
        
        def backtrack(i):
            if i == len(ms):
                return True
            
            for j in range(4):
                
                if sides[j] + ms[i] <= l:
                    sides[j] += ms[i]
                    
                    if backtrack(i + 1):
                        return True
                    
                    sides[j] -= ms[i]
            
            return False
        
        return backtrack(0)


