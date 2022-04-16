#User function Template for python3

class Solution:
    
    #Function to count paths between two vertices in a directed graph.
    def countPaths(self, V, adj, source, destination):
        
        count = 0
        visited = {}
        
        def dfs(i):
            if i == destination:
                nonlocal count
                count += 1
                return
                
            for j in adj[i]:
                if not visited.get(j):
                    # visited[j] = True
                    dfs(j)
        
        # visited[source] = True
        dfs(source)
        
        return count
        
#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		source, destination = map(int, input().split())
		ob = Solution()
		print(ob.countPaths(V, adj,source,destination))
        

# } Driver Code Ends