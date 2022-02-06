

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		nums2 = [(i, nums[i]) for i in range(len(nums))]
		nums2.sort(key = lambda x: x[1])
		count = 0
		i = 0
# 		print(nums2)
		while (i < len(nums)):
		    if (i != nums2[i][0]):
		        count += 1
		        j = nums2[i][0]
		        nums2[i], nums2[j] = nums2[j], nums2[i]
		    else:
		        i += 1
		return count

#{ 
#  Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends