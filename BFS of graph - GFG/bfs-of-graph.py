#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        traversal = []
        visited = {}
        q1 = [0]
        
        while (len(q1)):
            q2 = []
            for idx in q1:
                if visited.get(idx, False):
                    continue
                visited[idx] = True
                traversal.append(idx)
                q2.extend(adj[idx])
            q1 = q2
        
        return traversal

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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends