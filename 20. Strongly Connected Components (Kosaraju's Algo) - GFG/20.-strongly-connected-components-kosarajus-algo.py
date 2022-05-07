#User function Template for python3
def dfs(g, i, r, vs):
    for j in g[i]:
        if j not in vs:
            vs.add(j)
            dfs(g, j, r, vs)
    r.append(i)
    return r

class Solution:
    
    def kosaraju(self, V, adj):
        st = []
        visited = set()
        
        for i in range(V):
            if i not in visited:
                visited.add(i)
                dfs(adj, i, st, visited)

        tadj = [[] for _ in range(V)]
        
        for i in range(V):
            for j in adj[i]:
                tadj[j].append(i)

        visited = set()
        count = 0
        while st:
            if st[-1] in visited:
                st.pop()
            else:
                visited.add(st[-1])
                dfs(tadj, st[-1], [], visited)
                count += 1
                st.pop()
        return count



#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends