class Solution:
    def isCycle(self, V, adj):
        visited = {}

        # for i in range(V):
        #     visited[i] = True
        #     q.append((i, -1))
            
        for i in range(V):
            visited[i] = True
            q = [(i, -1)]
            while len(q):
                q2 = []
                for v, p in q:
                    for a in adj[v]:
                        if not visited.get(a):
                            visited[a] = True
                            q2.append((a, v))
                        elif a != p and p != -1:
                            return True
                q = q2


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