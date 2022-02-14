#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        xor = 0
        
        for i in range(n):
            xor ^= (i + 1)
            xor ^= arr[i]
        
        k = 0
        while not (xor & (1 << k)):
            k += 1
        
        xor1 = 0
        xor2 = 0
        
        for i in range(n):
            if (arr[i] & (1 << k)):
                xor1 ^= arr[i]
            else:
                xor2 ^= arr[i]
            
            if ((i + 1) & (1 << k)):
                xor1 ^= (i + 1)
            else:
                xor2 ^= (i + 1)
        
        if xor1 in arr:
            return xor1, xor2
        else:
            return xor2, xor1
    
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends