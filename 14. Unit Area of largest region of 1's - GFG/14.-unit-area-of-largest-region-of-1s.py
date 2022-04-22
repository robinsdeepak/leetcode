class Solution:

    #Function to find unit area of the largest region of 1s.
    def findMaxArea(self, grid):
    
        visited = set()
        m, n = len(grid), len(grid[0])
        
        def bfs(X, Y):
            area = 0
            
            q = [(X, Y)]
            
            while len(q):
                q2 = set()
                
                for x, y in q:
                    area += 1
                    
                    nbrs = [
                        (x+1, y), (x, y+1), (x-1, y), (x, y-1),
                        (x+1, y+1),(x+1, y-1),(x-1, y+1),(x-1, y-1),
                    ]
                    
                    for i, j in nbrs:
                        if 0 <= i < m and 0 <= j < n and grid[i][j] and \
                        (i, j) not in visited:
                            visited.add((i, j))
                            q2.add((i, j))
                            
                q = q2
            # print(X, Y, area)
            return area
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited:
                    visited.add((i, j))
                    ans = max(ans, bfs(i, j))
        return ans


#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.findMaxArea(grid)
		print(ans)

# } Driver Code Ends