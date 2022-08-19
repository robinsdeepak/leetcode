class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        f = collections.Counter(nums)
        
        s = []
        
        for x in nums:          
            for i in range(len(s) - 1, -1, -1):
                if s[i][0] == x - 1:
                    s[i][0] += 1
                    s[i][1] += 1
                    break
            else:
                s.append([x, 1])
                # s.sort(key=lambda e: e[1])
        
        for n, c in s:
            if c < 3:
                return False
        
        return True
