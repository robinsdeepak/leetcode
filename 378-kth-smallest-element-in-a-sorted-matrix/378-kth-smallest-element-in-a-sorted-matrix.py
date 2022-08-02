class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return self.solution_2(matrix, k)
    
    def solution_1(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        h = []
        for r in range(m):
            for c in range(n):
                heappush(h, -matrix[r][c])
                
                if len(h) > k:
                    heappop(h)
        
        return -h[0]
    
    def solution_2(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        
        def countLessOrEqual(x):
            count = 0
            c = n - 1
            for r in range(m):
                while c >= 0 and matrix[r][c] > x:
                    c -= 1
                count += (c + 1)
            return count
        
        l, h = matrix[0][0], matrix[-1][-1]
        
        ans = -1
        
        while l <= h:
            mid = (l + h) // 2
            if countLessOrEqual(mid) >= k:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        
        return ans
    
