#User function Template for python3

class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        # code here
        visited  = {}
        q = [(0, 0)]
        visited[0] = True
        
        while len(q):
            q2 = []
            
            for i, d in q:
                
                if i == X:
                    return d
                
                for j in adj[i]:
                    if not visited.get(j):
                        visited[j] = True
                        q2.append((j, d + 1))
            q = q2
            
        return -1

        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        X=int(input())
        ob = Solution()
        
        print(ob.nodeLevel(V, adj, X))
# } Driver Code Ends