#User function Template for python3

class Solution:
    def largestNum(self,n,s):
        d, r = divmod(s, 9)
        min_digit = (d + (r > 0))
        if n < min_digit: 
            return -1
        
        padding = n - min_digit
        
        ans = ("9" * d)+ (str(r) if r > 0 else "") + ("0" * padding)
        
        return ans
        
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,s = map(int,input().strip().split())
        ob = Solution()
        print(ob.largestNum(n,s))
# } Driver Code Ends