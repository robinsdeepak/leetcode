#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to check if a string is subsequence of other string.
    def isSubSequence(self, A, B):
        i = 0
        for c in B:
            if c == A[i]:
                i += 1
            if i == len(A):
                return True
        return False

#{ 
#Driver Code Starts.

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        A,B = input().split()
        ob = Solution()
        if (ob.isSubSequence(A,B)):
            print("True")
        else:
            print("False")
#} Driver Code Ends