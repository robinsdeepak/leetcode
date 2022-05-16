class Solution:
    def isBipartite(self, V, adj):
        colors = {}
        
        def dfs(x, c):

            if x in colors: 
                return colors[x] == c
            
            colors[x] = c
            
            for node in adj[x]:
                if not dfs(node, abs(1 - c)):
                    return False
            
            return True
            
        for i in range(V):
            if i not in colors:
                if not dfs(i, 0):
                    # print(i)
                    return False
        
        return True


#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends