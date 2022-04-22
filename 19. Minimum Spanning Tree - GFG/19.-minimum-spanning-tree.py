#User function Template for python3

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        mset = [False] * V
        keys = [float('inf')] * V
        keys[0] = 0
        ans = 0

        mat = [[0] * V for _ in range(V)]
        
        for i in range(len(adj)):
            for j, w in adj[i]:
                mat[i][j] = mat[j][i] = w
        
        for i in range(V):
            minSpanId = -1
            for j in range(V):
                if not mset[j] and (minSpanId == -1 or keys[minSpanId] > keys[j]):
                    minSpanId = j
                    
            ans += keys[minSpanId]
            mset[minSpanId] = True
                
            for j in range(V):
                if not mset[j] and mat[minSpanId][j]:
                    keys[j] = min(keys[j], mat[minSpanId][j])
        
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends