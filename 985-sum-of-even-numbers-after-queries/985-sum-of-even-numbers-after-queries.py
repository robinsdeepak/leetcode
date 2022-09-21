class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        es = sum(x for x in nums if x % 2 == 0)
        ans = []
        for v, i in queries:
            if nums[i] % 2 == 0:
                if v % 2 == 0:
                    es += v
                else:
                    es -= nums[i]
            else:
                if v % 2 != 0:
                    es += (v + nums[i])
            
            nums[i] += v
            ans.append(es)
        
        return ans

