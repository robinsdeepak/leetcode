#User function Template for python3

class Solution:
    
    def __init__(self):
        self.visited = {}
        self.traversal = []
    
    def dfs(self, idx, adj):
        if self.visited.get(idx, False):
            return 
        
        self.traversal.append(idx)
        self.visited[idx] = True
        
        for idxx in adj[idx]:
            self.dfs(idxx, adj)
        
        
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        self.dfs(0, adj)
        
        return self.traversal
        

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends