class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = [0] * n
        rmax = [0] * n
        
        lmax[0] = height[0]
        rmax[-1] = height[-1]
        
        for i in range(1, n):
            lmax[i] = max(height[i], lmax[i - 1])
        
        for i in range(n - 2, -1, -1):
            rmax[i] = max(height[i], rmax[i + 1])
        
        tp = 0
        
        for i in range(1, n - 1):
            tp += min(rmax[i], lmax[i]) - height[i]
            
        return tp
