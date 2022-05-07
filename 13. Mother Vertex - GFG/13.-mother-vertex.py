

class Solution:
    
    #Function to find a Mother Vertex in the Graph.
	def findMotherVertex(self, V, adj):
	    
        def dfs(i, visited, st):
            for j in adj[i]:
                if j not in visited:
                    visited.add(j)
                    dfs(j, visited, st)
            if st is not None: st.append(i)
        
        st = []
        visited = set()
        for i in range(V):
            if i not in visited:
                visited.add(i)
                dfs(i, visited, st)
        
        top = st[-1]
        visited = {top}
        dfs(top, visited, None)

        return top if len(visited) == V else -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		obj = Solution()
		ans = obj.findMotherVertex(V, adj)
		print(ans)
# } Driver Code Ends