class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        prefixSum = [0] * n
        
        for i in range(n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]
        
        lastIdx = {}
        
        maxSum = 0
        currSum = 0
        start = 0
        
        for i, x in enumerate(nums):
            if x in lastIdx and lastIdx[x] >= start:
                start = lastIdx[x] + 1

            currSum = (prefixSum[i] - prefixSum[start - 1]) if start > 0 else prefixSum[i]
            maxSum = max(currSum, maxSum)
            
            lastIdx[x] = i
        
        return maxSum
