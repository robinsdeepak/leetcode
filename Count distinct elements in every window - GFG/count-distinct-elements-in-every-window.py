
class Solution:
    
    def __init__(self):
        self.freq = {}
    
    def add(self, freq, num):
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    def remove(self, freq, num):
        if freq[num] == 1:
            del freq[num]
        else:
            freq[num] -= 1
            
    def countDistinct(self, A, N, K):
        
        freq = {}

        for i in range(K):
            self.add(freq, A[i])
        
        ans = [len(freq)]

        for i in range(K, len(A)):
            self.remove(freq, A[i - K])
            self.add(freq, A[i])
            ans.append(len(freq))

        return ans
        
        
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends