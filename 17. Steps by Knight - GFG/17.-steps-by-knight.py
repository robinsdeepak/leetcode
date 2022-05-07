
class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
        
        q = [(*KnightPos, 0)]
        
        visited = {tuple(KnightPos)}
        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2]
        
        while len(q):
            q2 = []
            for x, y, d in q:
                if TargetPos == [x, y]:
                    return d

                for i in range(8):
                    xx = x + dx[i]
                    yy = y + dy[i]

                    if (xx, yy) not in visited:
                        visited.add((xx, yy))
                        q2.append((xx, yy, d + 1))
            q = q2

        return -1



#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		KnightPos = list(map(int, input().split()))
		TargetPos = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
		print(ans)

# } Driver Code Ends