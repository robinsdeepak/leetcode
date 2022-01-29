class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        
        left[0] = -1
        right[-1] = n
        
        for i in range(1, n):
            p = i - 1    
            while (p >= 0 and heights[p] >= heights[i]):
                p = left[p]
            left[i] = p
        
        for i in range(n - 2, -1, -1):
            p = i + 1
            while (p < n and heights[p] >= heights[i]):
                p = right[p]
            right[i] = p
        
        max_area = 0
        for i in range(n):
            curr_area = heights[i] * (right[i] - left[i] - 1)
            max_area = max(max_area, curr_area)
            
        return max_area
