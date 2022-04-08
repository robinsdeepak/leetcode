#User function Template for python3

class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        visited = {}
        recAct = {}
        def dfs(x):
            visited[x] = True
            recAct[x] = True
            for a in adj[x]:
                if not visited.get(a) and dfs(a):
                    return True
                if recAct.get(a):
                    return True
            recAct[x] = False
            return False
        
        for i in range(V):
            if not visited.get(i):
                if dfs(i):
                    # print(i)
                    return True
        return False
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

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
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends