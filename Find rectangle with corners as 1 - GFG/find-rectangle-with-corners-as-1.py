#User function Template for python3

class Solution: 
    
    def ValidCorner(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        
        for r1 in range(row):
            for r2 in range(r1 + 1, row):
                count = 0
                for c in range(col):
                    count += (matrix[r1][c] & matrix[r2][c])
                if count > 1:
                    # print(r1, r2)
                    return True
        return False


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		r = int(input())
		c = int(input())
		line = input().strip().split()
		mat = [ [0 for _ in range(c)] for _ in range(r) ]
		for i in range(r):
			for j in range(c):
				mat[i][j] = int( line[i*c+j] )
		ob=Solution()
		if (ob.ValidCorner(mat)): 
			print("Yes") 
		else: 
			print("No") 


# } Driver Code Ends