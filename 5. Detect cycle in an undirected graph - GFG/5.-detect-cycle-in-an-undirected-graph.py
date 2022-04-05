class Solution:
    def isCycle(self, V, adj):
        visited = {}
        def isCycleRec(v, parent):
            visited[v] = True
            for a in adj[v]:
                if not visited.get(a):
                    if isCycleRec(a, v):
                        return True
                elif a != parent:
                    return True
            return False
        
        for i in range(V):
            if not visited.get(i):
                if isCycleRec(i, -1):
                    return True
        return False
        
        
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
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends