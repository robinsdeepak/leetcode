class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        m = {}
        for x in nums:
            if not x in m:
                m[x] = 0
            m[x] += 1
        
        if k == 0:
            for key, val in m.items():
                if val > 1:
                    count += 1
        else:
            for key, val in m.items():
                if key + k in m:
                    count += 1
        return count

