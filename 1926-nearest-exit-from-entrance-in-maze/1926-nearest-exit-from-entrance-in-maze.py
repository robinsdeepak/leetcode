class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        m, n = len(maze), len(maze[0])
        visited = {}
        x, y = entrance
        
        q = [(x, y, 0)]
        visited[(x, y)] = True
        
        while len(q):
            q2 = []
            
            for x, y, d in q:
                if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and [x, y] != entrance:
                    return d
                
                nbrs = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
                
                
                for i, j in nbrs:
                    if 0 <= i < m and 0 <= j < n and not visited.get((i, j)) and maze[i][j] == '.':
                        visited[(i, j)] = True
                        q2.append((i, j, d + 1))
                
            q = q2
        
        return -1
