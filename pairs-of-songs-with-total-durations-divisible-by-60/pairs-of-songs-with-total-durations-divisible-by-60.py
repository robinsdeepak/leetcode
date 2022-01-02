class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        m = [0] * 60
        res = 0
        for t in time: 
            res += m[(60 - t % 60) % 60]
            m[t % 60] += 1
        return res