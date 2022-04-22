class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        ind = {i: 0 for i in range(V)}
        for i in range(len(adj)):
            for j in adj[i]:
                ind[j] += 1
        
        q = [i for i, j in ind.items() if j == 0]
        ans = []
        while len(q):
            q2 = []
            
            for i in q:
                ans.append(i)
                for j in adj[i]:
                    ind[j] -= 1
                    if ind[j] == 0:
                        q2.append(j)
            q = q2
        
        return ans



#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends