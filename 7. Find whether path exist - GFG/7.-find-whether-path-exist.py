

class Solution:
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
		m, n = len(grid), len(grid[0])
		
		source = None
		
		for i in range(m):
		    for j in range(n):
                if grid[i][j] == 1:
                    source = (i, j)
                    break
        
        q = [source]
        
        while(len(q)):
            q2 = []
            for x, y in q:
                if grid[x][y] == 2:
                    return True
                grid[x][y] = 0
                
                nbrs = [(x+1, y), (x, y+1), (x-1,y), (x, y-1)]
                
                for r, c in nbrs:
                    if 0 <= r < m and 0 <= c < n and grid[r][c]:
                        q2.append((r, c))
            q = q2
        
        return False
        
#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.is_Possible(grid)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends