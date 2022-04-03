#User function Template for python3
import sys
sys.setrecursionlimit(100000)

class Solution:
    
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])

        def solve(x, y):

            grid[x][y] = 0

            coords = [(x + i, y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i,j) != (0, 0)]
            
            for r, c in coords:
                if 0 <= r < m and 0 <= c < n and grid[r][c]:
                    solve(r, c)
            
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    count += 1
                    solve(i, j)
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