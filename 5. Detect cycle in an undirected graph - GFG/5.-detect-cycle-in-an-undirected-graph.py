class Solution:
    def isCycle(self, V, adj):
        # print(V)
        # print(adj)
        visited = {};
        def isCycleRec(i, parent):
            visited[i] = True
            for a in adj[i]:
                if not visited.get(a):
                    if(isCycleRec(a, i)):
                        return True
                elif (a != parent):
                    return True
            return False

        for k in range(V):
            if not visited.get(k):
                if (isCycleRec(k, -1)):
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