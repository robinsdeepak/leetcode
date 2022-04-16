class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		inf = float('inf')
		m, n = len(grid), len(grid[0])
		dist = [[inf] * n for i in range(m)]
		
		q = []
		for i in range(m):
		    for j in range(n):
		        if grid[i][j] == 1:
		            q.append((i, j, 0))
		            dist[i][j] = 0
        
        while len(q):
            q2 = []
            
            for i, j, d in q:
                dist[i][j] = min(dist[i][j], d)
                
                nbrs = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
                
                for x, y in nbrs:
                    if 0 <= x < m and 0 <= y < n and dist[x][y] == inf:
                        q2.append((x, y, d + 1))
            q = q2
            
        # for r in dist:
        #     print(r)
            
        return dist
            
		            
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
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends