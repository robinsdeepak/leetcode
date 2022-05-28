#User function Template for python3

class Solution:
    
    def __init__(self):
        self.parent = None
        self.ranks = None
    
    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x
        
    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)
        
        if(x_rep==y_rep):
            return
        
        if (self.ranks[x_rep]<self.ranks[y_rep]):
            self.parent[x_rep] = y_rep
        
        elif (self.ranks[y_rep]<self.ranks[x_rep]):
            self.parent[y_rep]=x_rep
        
        else: 
            self.parent[y_rep] = x_rep
            self.ranks[x_rep] += 1
    
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, v, adj):
    
        # kruskal algorithm
        edges = []
        
        for i in range(len(adj)):
            for j, w in adj[i]:
                edges.append((i, j, w))
                edges.sort(key=lambda x: x[2])
        
        self.parent = list(range(v))
        self.ranks = [0] * v
        
        i, s = 0, 0
        
        result = 0
        
        while s < v - 1  and i < len(edges):
            a, b, w = edges[i]
            
            x = self.find(a)
            y = self.find(b)
            
            if (x != y):
                self.union(x, y)
                result += w
                s += 1
            
            i += 1
        
        return result
        
        
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
