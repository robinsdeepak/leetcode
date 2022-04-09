class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
                
        ans = []
        for i in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            ans.append(i[0])
            if len(ans) == k:
                break
    
        return ans
