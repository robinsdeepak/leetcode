#User function Template for python3

class Solution:
    def maxSubArraySum(self, arr, n):
        max_sum = float('-inf')
        curr_sum = 0
        
        for i in range(n):
            curr_sum += arr[i]
            max_sum = max(curr_sum, max_sum)
            curr_sum = max(0, curr_sum)
        return max_sum

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends