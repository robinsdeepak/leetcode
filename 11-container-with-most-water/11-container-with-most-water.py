class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_ar = 0;
        i = 0; 
        j = n - 1;
        
        while (i < j):
            max_ar = max(max_ar, min(height[i], height[j]) * (j - i));
            if (height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return max_ar
