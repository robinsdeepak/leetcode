class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l = [p[0] for p in points]
        l.sort()
        
        ans = 0
        for i in range(len(l) - 1):
            ans = max(ans, l[i + 1] - l[i])
        
        return ans
