class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        h = []
        for r in range(m):
            for c in range(n):
                heappush(h, -matrix[r][c])
                
                if len(h) > k:
                    heappop(h)
        
        return -h[0]
