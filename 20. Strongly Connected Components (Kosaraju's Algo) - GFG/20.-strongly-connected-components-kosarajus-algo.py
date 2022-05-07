#User function Template for python3
def dfs(g, i, st, vs):
    for j in g[i]:
        if j not in vs:
            vs.add(j)
            dfs(g, j, st, vs)
    st.append(i)
    return st

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
        st.reverse()
        for x in st:
            if x not in visited:
                visited.add(x)
                dfs(tadj, x, [], visited)
                count += 1
                
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