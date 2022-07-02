
class Solution:
    def maxArea(self, h: int, w: int, hct: List[int], vct: List[int]) -> int:
        hct.sort()
        vct.sort()
        mod = 10 ** 9 + 7
        
        mh = max(hct[0], h - hct[-1])
        mv = max(vct[0], w - vct[-1])
        
        for i in range(1, len(hct)):
            mh = max(mh, hct[i] - hct[i - 1])
        
                
        for i in range(1, len(vct)):
            mv = max(mv, vct[i] - vct[i - 1])
            
        
        return (mh * mv) % mod

