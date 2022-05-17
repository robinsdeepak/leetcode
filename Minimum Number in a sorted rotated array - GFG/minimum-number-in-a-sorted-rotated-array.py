#User function Template for python3


class Solution:
    
    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr,low,high):
        
        n = len(arr)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            # print(low, mid, high)
            
            if (mid == 0 and arr[0] < arr[n - 1]) or (arr[mid] < arr[mid - 1]):
                return arr[mid]
            
            if arr[mid] > arr[high]:
                low = mid + 1
            elif arr[low] > arr[mid]:
                high = mid
            
            elif arr[low] <= arr[mid] <= arr[high]:
                high = mid - 1
        
        return -1
        
        #{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.minNumber(A,0,N-1))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends