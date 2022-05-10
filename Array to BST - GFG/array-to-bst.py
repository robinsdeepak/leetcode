class Solution:
    def sortedArrayToBST(self, nums):
        ans = []
        
        def fn(s, e):
            if s > e: return
            m = (s + e) // 2
            
            ans.append(nums[m])
            
            fn(s, m - 1)
            fn(m + 1, e)
        
        fn(0, len(nums) - 1)
        return ans
	        

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.sortedArrayToBST(nums)
		for _ in ans:
			print(_, end = " ")
		print()

# } Driver Code Ends