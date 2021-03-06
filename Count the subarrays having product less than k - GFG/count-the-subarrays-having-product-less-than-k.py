#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        l, r = 0, 0
        prod = 1
        count = 0
        
        for r in range(n):
            prod *= a[r]
            
            while l < r and prod > k:
                prod = prod / a[l]
                l += 1
            
            if prod < k:
                count += (r - l + 1)
                
        return count


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends