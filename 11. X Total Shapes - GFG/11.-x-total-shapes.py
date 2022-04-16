

class Solution:
    
    #Function to find the number of 'X' total shapes.
	def xShape(self, grid):
		n, m = len(grid), len(grid[0])
		
		
        def dfs(x, y):
            grid[x][y] = '0'
            
            nbrs = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
            
            for i, j in nbrs:
                if 0 <= i < n and 0 <= j < m and grid[i][j] == 'X':
                    dfs(i, j)
        
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'X':
                    count += 1
                    dfs(i, j)
        return count

#{ 
#  Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = [['#' for i in range(m)] for j in range(n)]
		for i in range(n):
			s = input().strip()
			for j in range(m):
				grid[i][j] = s[j]
		obj = Solution()
		ans = obj.xShape(grid)
		print(ans)
# } Driver Code Ends