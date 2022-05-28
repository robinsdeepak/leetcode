#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
	    n = len(matrix)
	    inf = float('inf')
	    
	    def get_(i, j):
	        return inf if matrix[i][j] == -1 else matrix[i][j]
	    
	    def set_(i, j, v):
	        matrix[i][j] = -1 if v == inf else v
	    
	    for k in range(n):
	        for i in range(n):
	            for j in range(n):
	                set_(i, j, min(get_(i, j), get_(i, k) + get_(k, j)))
	   

#{ 
#  Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends