class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        
        rf = list(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        
        ans = []
        for i in range(k):
            ans.append(rf[i][0])
        
        return ans
