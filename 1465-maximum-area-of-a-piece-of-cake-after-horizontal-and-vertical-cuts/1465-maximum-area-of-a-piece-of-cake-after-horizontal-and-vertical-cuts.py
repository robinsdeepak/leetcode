
class Solution:
    def maxArea(self, h: int, w: int, hct: List[int], vct: List[int]) -> int:
        hct.sort()
        vct.sort()
        mod = 10 ** 9 + 7
        
        if hct[0] != 0:
            hct.insert(0, 0)
        
        if hct[-1] != w:
            hct.append(h)
            
        if vct[0] != 0:
            vct.insert(0, 0)
        
        if vct[-1] != w:
            vct.append(w)
        
        mh = 1
        
        for i in range(1, len(hct)):
            mh = max(mh, hct[i] - hct[i - 1])
        
        
        mv = 1
        
        for i in range(1, len(vct)):
            mv = max(mv, vct[i] - vct[i - 1])
            
        
        return (mh * mv) % mod

