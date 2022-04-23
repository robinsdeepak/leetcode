class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        mset = [False] * V
        d = [float('inf')] * V
        d[S] = 0
        
        mat = [[0] * V for _ in range(V)]
        
        for i in range(V):
            for j, w in adj[i]:
                mat[i][j] = mat[j][i] = w
        
        for i in range(V):
            minDistId = -1
            
            for j in range(V):
                if not mset[j] and (minDistId == -1 or d[j] < d[minDistId]):
                    minDistId = j
            
            mset[minDistId] = True
            
            for j in range(V):
                if not mset[j] and mat[minDistId][j] != 0 and \
                d[j] > d[minDistId] + mat[minDistId][j]:
                    
                    d[j] = d[minDistId] + mat[minDistId][j]
            
        return d
        
        #{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends