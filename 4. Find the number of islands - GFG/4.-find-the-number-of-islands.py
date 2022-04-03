#User function Template for python3
import sys
sys.setrecursionlimit(100000)

class Solution:
    
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]
        
        def solve(x, y):

            visited[x][y] = True

            coords = [(x + i, y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i,j) != (0, 0)]
            
            for r, c in coords:
                # print(r, c)
                if 0 <= r < m and 0 <= c < n and grid[r][c] and not visited[r][c]:
                    solve(r, c)
            
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    count += 1
                    solve(i, j)
        # solve(0, 1)
        # print(visited)
        return count
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends