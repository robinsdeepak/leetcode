class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def rec(idx, path):
            if not idx:
                ans.add(tuple(path))
            
            for i in idx:
                tmp = idx.copy()
                tmp.remove(i)
                rec(tmp, path + [nums[i]])
        
        rec(set(range(len(nums))), [])
        return ans
