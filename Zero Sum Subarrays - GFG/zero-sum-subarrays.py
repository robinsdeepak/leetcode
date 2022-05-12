#User function Template for python3

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        s = [0]
        m = {0: 1}
        count = 0
        for x in arr:
            c = s[-1] + x
            s.append(c)
            if c in m:
                count += m[c]
            else:
                m[c] = 0
            m[c] += 1
        return count
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends