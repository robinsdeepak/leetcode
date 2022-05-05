class Solution:
    def findPages(self,A, N, M):
        if N < M: return -1
        
        min_ = max(A)
        sum_ = sum(A)
        
        def isPossible(s):
            st_count = 0
            curr_pages = 0
            
            for i in range(N):
                x = A[i]
                if curr_pages + x <= s:
                    curr_pages += x
                else:
                    curr_pages = x
                    st_count += 1
                if st_count == M and i < N:
                    return False
            return True
        
        
        l = min_
        h = sum_
        ans = -1
        # print(l, h)
        while (l <= h):
            mid = (l + h) // 2
            p = isPossible(mid)
            # print(mid, p)
            if p:
                h = mid - 1
                ans = mid
            else:
                l = mid + 1
        
        return ans

        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends