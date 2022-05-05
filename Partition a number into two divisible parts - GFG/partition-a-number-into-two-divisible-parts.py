#User function Template for python3
class Solution:
    def stringPartition(ob,S,a,b):
        # Code here
        n = len(S)
        for i in range(1, n):
            x, y = S[:i], S[i:]
            if (int(x) % a == 0 and int(y) % b == 0):
                return x + " " + y
        return "-1"

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,a,b=map(str,input().strip().split(" "))
        a=int(a)
        b=int(b)
        ob = Solution()
        print(ob.stringPartition(S,a,b))
# } Driver Code Ends